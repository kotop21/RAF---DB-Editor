import json
import re
from pathlib import Path
from colorama import Fore, Style
from tqdm import tqdm
from services.dat_json_utils.save_objects_json import save_objects_json
from config import UNPACK_FOLDER, DB_FOLDER, JSON_SUFFIX


def load_schema(schema_path: Path):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    fields = {k: int(v, 16) for k, v in schema["fields"].items()}
    pattern = re.compile(schema.get("name_pattern", rb"A - [\x20-\x7E]{5,60}?").encode() if isinstance(schema.get("name_pattern"), str) else schema.get("name_pattern"))
    return pattern, fields


def dat_to_json_generic(dat_path: Path, schema_path: Path):
    pattern, fields = load_schema(schema_path)

    with open(dat_path, "rb") as f:
        data = f.read()

    objects = []
    for idx, match in enumerate(pattern.finditer(data), start=1):
        start = match.start()
        name_bytes = data[start:start + 0x60]
        try:
            name = name_bytes.decode("ascii", errors="ignore").strip("\x00 ")
        except UnicodeDecodeError:
            continue

        obj = {"id": idx, "name": name}
        for key, offset in fields.items():
            value_offset = start + offset
            if value_offset + 4 <= len(data):
                obj[key] = int.from_bytes(data[value_offset:value_offset + 4], "little")
            else:
                obj[key] = None
        objects.append(obj)

    save_objects_json(objects, dat_path)
    print(Fore.GREEN + f"✅ Exported {dat_path.name} to JSON using schema {schema_path.name}" + Style.RESET_ALL)


def json_to_dat_generic(dat_path: Path, schema_path: Path):
    pattern, fields = load_schema(schema_path)
    json_file = UNPACK_FOLDER / (Path(dat_path).stem + JSON_SUFFIX)

    if not json_file.exists():
        print(Fore.RED + f"❌ JSON file {json_file} not found!" + Style.RESET_ALL)
        return

    with open(json_file, "r", encoding="utf-8") as f:
        objects = json.load(f)

    db_bytes = bytearray(Path(dat_path).read_bytes())
    updated = 0

    for obj in tqdm(objects, desc=f"Updating {dat_path.name}", colour="cyan", ncols=80):
        name = obj.get("name")
        if not name:
            continue

        name_bytes = name.encode("ascii").ljust(0x60, b"\x00")
        start = db_bytes.find(name_bytes)
        if start == -1:
            tqdm.write(Fore.RED + f"❌ Object '{name}' not found in {dat_path.name}" + Style.RESET_ALL)
            continue

        changed = False
        for key, offset in fields.items():
            value = obj.get(key)
            if isinstance(value, int):
                db_bytes[start + offset:start + offset + 4] = value.to_bytes(4, "little")
                changed = True

        if changed:
            updated += 1

    Path(dat_path).write_bytes(db_bytes)
    print(Fore.GREEN + f"✅ {dat_path.name}: updated {updated}/{len(objects)} objects." + Style.RESET_ALL)

