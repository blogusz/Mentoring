import json
import os
from typing import Any


def make_directory(path: str) -> bool:
    """
    Create directory if it doesn't exist.
    
    :param path: Path where the folder will be created
    :return: True if successful, False otherwise
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            return True
        except OSError as e:
            print(f'Error while making directory {path}: {e}')
            return False
    return True


def save_json_file(data: Any, output_path: str, output_file: str) -> None:
    """
    Save data to JSON file.

    :param data: Data to be saved
    :param output_path: Path where the file will be saved
    :param output_file: Name of the output file
    """
    make_directory(output_path)

    output_file_path = os.path.join(output_path, output_file)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f'Data saved to: {output_file_path}')