import json
from pathlib import Path

def save_objects_json(objects, filename="objects.json"):
    """
    objects: список кортежей (id, name, hp)
    filename: имя файла 
    """
    root_path = Path.cwd()
    path = root_path / filename
     
    data = [
        {"id": obj_id, "name": name, "hp": hp}
        for obj_id, name, hp in objects
    ]
    
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return path
