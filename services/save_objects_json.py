import json
from pathlib import Path
from config import UNPACK_FOLDER

def save_objects_json(data, dat_file_path, json_suffix=".json"):
    """
    Save prepared data to a JSON file corresponding to the given .dat file.
    JSON file is stored in UNPACK_FOLDER with the same name as the .dat file.
    
    Parameters:
        data (list): List of dictionaries to save in JSON.
        dat_file_path (str | Path): Path to the original .dat file.
        json_suffix (str): Suffix for the JSON file (default ".json").
    """
    UNPACK_FOLDER.mkdir(parents=True, exist_ok=True)
    path = UNPACK_FOLDER / (Path(dat_file_path).stem + json_suffix)

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return path
