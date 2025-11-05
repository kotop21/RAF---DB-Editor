import json
from pathlib import Path
from colorama import Fore, Style
from tqdm import tqdm

from config import HP_OFFSET, DAMAGE_OFFSET, DB_PATH, JSON_SUFFIX, UNPACK_FOLDER, GOLD_OFFSET, WOOD_OFFSET


def db_objects_json_to_dat():
    dat_file = DB_PATH[0]
    json_file = UNPACK_FOLDER / (Path(dat_file).stem + JSON_SUFFIX)
    if not json_file.exists():
        print(Fore.RED + f"❌ File {json_file} not found!" + Style.RESET_ALL)
        return

    with open(json_file, "r", encoding="utf-8") as f:
        objects = json.load(f)

    db_bytes = bytearray(Path(dat_file).read_bytes())
    updated = 0
    total = len(objects)

    for obj in tqdm(objects, desc=f"Updating {dat_file}", colour="cyan", ncols=80):
        name = obj.get("name")
        hp = obj.get("hp")
        damage = obj.get("damage")
        if not name:
            continue

        name_bytes = name.encode("ascii").ljust(0x60, b"\x00")
        start = db_bytes.find(name_bytes)
        if start == -1:
            start = db_bytes.find(name.encode("ascii"))
            if start == -1:
                tqdm.write(Fore.RED + f"❌ Object '{name}' not found in {dat_file}!" + Style.RESET_ALL)
                continue

        object_updated = False
        if isinstance(hp, int):
            db_bytes[start + HP_OFFSET:start + HP_OFFSET + 4] = hp.to_bytes(4, "little")
            object_updated = True
        if isinstance(damage, int):
            db_bytes[start + DAMAGE_OFFSET:start + DAMAGE_OFFSET + 4] = damage.to_bytes(4, "little")
            object_updated = True
        if object_updated:
            updated += 1

    Path(dat_file).write_bytes(db_bytes)
    print(Fore.GREEN + f"✅ {dat_file}: Applied changes {updated}/{total}" + Style.RESET_ALL)


def db_techtree_json_to_dat():
    dat_file = DB_PATH[1]
    json_file = UNPACK_FOLDER / (Path(dat_file).stem + JSON_SUFFIX)
    if not json_file.exists():
        print(Fore.RED + f"❌ File {json_file} not found!" + Style.RESET_ALL)
        return

    with open(json_file, "r", encoding="utf-8") as f:
        objects = json.load(f)

    db_bytes = bytearray(Path(dat_file).read_bytes())
    updated = 0
    total = len(objects)

    for obj in tqdm(objects, desc=f"Updating {dat_file}", colour="cyan", ncols=80):
        name = obj.get("name")
        gold = obj.get("gold")
        wood = obj.get("wood")
        if not name:
            continue

        name_bytes = name.encode("ascii").ljust(0x60, b"\x00")
        start = db_bytes.find(name_bytes)
        if start == -1:
            start = db_bytes.find(name.encode("ascii"))
            if start == -1:
                tqdm.write(Fore.RED + f"❌ Object '{name}' not found in {dat_file}!" + Style.RESET_ALL)
                continue

        object_updated = False
        if isinstance(gold, int):
            db_bytes[start + GOLD_OFFSET:start + GOLD_OFFSET + 4] = gold.to_bytes(4, "little")
            object_updated = True
        if isinstance(wood, int):
            db_bytes[start + WOOD_OFFSET:start + WOOD_OFFSET + 4] = wood.to_bytes(4, "little")
            object_updated = True
        if object_updated:
            updated += 1

    Path(dat_file).write_bytes(db_bytes)
    print(Fore.GREEN + f"✅ {dat_file}: Applied changes {updated}/{total}" + Style.RESET_ALL)
