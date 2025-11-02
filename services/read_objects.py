import re 

def read_objects(path):
    with open(path, "rb") as f:
        data = f.read()

    pattern = re.compile(rb"A - [\x20-\x7E]{5,60}?")  
    objects = []

    for idx, match in enumerate(pattern.finditer(data), start=1):
        start = match.start()
        name_bytes = data[start:start + 0x60]  
        hp_offset = start + 0x78
        if hp_offset + 4 <= len(data):
            hp_bytes = data[hp_offset:hp_offset + 4]
            hp = int.from_bytes(hp_bytes, "little")
            try:
                name = name_bytes.decode("ascii", errors="ignore").strip("\x00 ")
                objects.append((idx, name, hp))
            except UnicodeDecodeError:
                continue

    return objects
