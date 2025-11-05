import re
from config import HP_OFFSET, DAMAGE_OFFSET


def dbobjects_read_binar(path):
    with open(path, "rb") as f:
        data = f.read()

    pattern = re.compile(rb"A - [\x20-\x7E]{5,60}?")
    objects = []

    for idx, match in enumerate(pattern.finditer(data), start=1):
        start = match.start()
        name_bytes = data[start:start + 0x60]

        # --- HP ---
        hp_offset = start + HP_OFFSET
        hp = int.from_bytes(data[hp_offset:hp_offset + 4], "little") if hp_offset + 4 <= len(data) else None

        # --- Damage ---
        damage_offset = start + DAMAGE_OFFSET
        damage = int.from_bytes(data[damage_offset:damage_offset + 4], "little") if damage_offset + 4 <= len(data) else None

        try:
            name = name_bytes.decode("ascii", errors="ignore").strip("\x00 ")
            objects.append((idx, name, hp, damage))
        except UnicodeDecodeError:
            continue

    return objects
