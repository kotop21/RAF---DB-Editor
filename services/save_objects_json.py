import json
from pathlib import Path

def save_objects_json(objects, filename="objects.json"):
    """
    objects: (id, name, hp, damage)
    """
    path = Path(filename)
     
    data = [
        {"id": obj_id, "name": name, "hp": hp, "damage": damage}
        for obj_id, name, hp, damage in objects
    ]
    
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return path

