import json
from pathlib import Path
from colorama import init, Fore, Style
from tqdm import tqdm

from services.read_objects import read_objects
from services.save_objects_json import save_objects_json

from config import HP_OFFSET, DAMAGE_OFFSET, JSON_PATH, DB_PATH

def dat_to_json():
    print(Fore.CYAN + "\n📦 Converting dbobjects.dat → objects.json..." + Style.RESET_ALL)
    objects = read_objects(DB_PATH)
    save_objects_json(objects, JSON_PATH)
    print(Fore.GREEN + f"✅ Successfully exported to {JSON_PATH}" + Style.RESET_ALL)

def json_to_dat():
    print(Fore.CYAN + "\n🔄 Applying changes from JSON to dat..." + Style.RESET_ALL)

    json_path = Path(__file__).parent.parent / JSON_PATH
    if not json_path.exists():
        print(Fore.RED + f"❌ File {JSON_PATH} not found!" + Style.RESET_ALL)
        return

    with open(json_path, "r", encoding="utf-8") as f:
        objects = json.load(f)

    db_bytes = bytearray(Path(DB_PATH).read_bytes())
    updated = 0
    total = len(objects)

    for obj in tqdm(objects, desc="Updating objects", colour="cyan", ncols=80):
        name = obj.get("name")
        hp = obj.get("hp")
        damage = obj.get("damage")

        if not name:
            continue

        name_bytes = name.encode("ascii").ljust(0x60, b"\x00")
        start = db_bytes.find(name_bytes)
        if start == -1:
            tqdm.write(Fore.RED + f"❌ Object '{name}' not found in binary file!" + Style.RESET_ALL)
            continue

        if isinstance(hp, int):
            db_bytes[start + HP_OFFSET:start + HP_OFFSET + 4] = hp.to_bytes(4, "little")
            updated += 1

        if isinstance(damage, int):
            db_bytes[start + DAMAGE_OFFSET:start + DAMAGE_OFFSET + 4] = damage.to_bytes(4, "little")
            updated += 1

    Path(DB_PATH).write_bytes(db_bytes)
    print(Fore.GREEN + f"\n✅ Successfully applied changes: {updated}/{total}" + Style.RESET_ALL)
