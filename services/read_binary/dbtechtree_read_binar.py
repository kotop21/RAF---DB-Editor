import re
from config import GOLD_OFFSET, WOOD_OFFSET

def dbtechtree_read_binar(path):
    with open(path, "rb") as f:
        data = f.read()

    pattern = re.compile(rb"A - [\x20-\x7E]{5,60}?")
    objects = []

    for idx, match in enumerate(pattern.finditer(data), start=1):
        start = match.start()
        name_bytes = data[start:start + 0x60]

        # --- Gold ---
        gold_offset = start + GOLD_OFFSET
        gold = int.from_bytes(data[gold_offset:gold_offset + 4], "little") if gold_offset + 4 <= len(data) else None

        # --- Wood ---
        wood_offset = start + WOOD_OFFSET
        wood = int.from_bytes(data[wood_offset:wood_offset + 4], "little") if wood_offset + 4 <= len(data) else None

        try:
            name = name_bytes.decode("ascii", errors="ignore").strip("\x00 ")
            objects.append((idx, name, gold, wood))
        except UnicodeDecodeError:
            continue

    return objects
