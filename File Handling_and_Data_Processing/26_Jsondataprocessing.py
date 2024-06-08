import json
from typing import Dict

def process_json(file_path: str) -> Dict:
    processed_data = {}
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        
        processed_data['name'] = data['name']
        processed_data['age'] = data['age']
        
    return processed_data



# Example:
file_path = "example.json"  # Replace with the actual file path
processed_data = process_json(file_path)
print(processed_data)
