from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


# Example:
file_path = "example.txt"  # Replace with the  file path
lines = ["This is line 1", "This is line 2", "This is line 3"]
write_file(file_path, lines)
print("File written successfully.")