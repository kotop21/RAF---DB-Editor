import json
from pathlib import Path

def load_objects_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_objects_json(objects, filename="objects.json"):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as f:
        json.dump(objects, f, indent=4, ensure_ascii=False)
    return path

