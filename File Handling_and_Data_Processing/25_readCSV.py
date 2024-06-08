import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    rows = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(dict(row))
    return rows


# Example :
file_path = "example.csv"  # Replace with the actual file path
data = read_csv(file_path)
for row in data:
    print(row)