from config import DB_PATH
from services.dat_json_utils.dat_to_json import dat_to_json
from services.read_binary.dbobjects_read_binar import dbobjects_read_binar
from services.read_binary.dbtechtree_read_binar import dbtechtree_read_binar

def dbobjects_to_json():
    objects = dbobjects_read_binar(DB_PATH[0])  
    data = [
        {"id": obj_id, "name": name, "hp": hp, "damage": damage}
        for obj_id, name, hp, damage in objects
    ]
    dat_to_json(DB_PATH[0], dbobjects_read_binar, data)  

def dbtechtree_to_json():
    objects = dbtechtree_read_binar(DB_PATH[1])

    data = [
        {"id": obj_id, "name": name, "gold": gold, "wood": wood}
        for obj_id, name, gold, wood in objects
    ]

    dat_to_json(DB_PATH[1], dbtechtree_read_binar, data)
