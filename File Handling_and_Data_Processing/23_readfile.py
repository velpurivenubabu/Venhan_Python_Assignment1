from typing import List # Import the list module


def read_file(file_path: str) -> List[str]:
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())  # Strip function removes  leading/trailing whitespaces.
    return lines



# Example :
file_path = "example.txt"  # Replace with the actual file path
lines = read_file(file_path)
print(lines)
