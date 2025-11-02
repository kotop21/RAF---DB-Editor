from pathlib import Path

def update_object_param(db_path, obj_name, param_offset, new_value):
    """
    Changes the value of a parameter in the binary file by object name and offset.
    param_offset - offset from the beginning of the object name (e.g. HP = 0x78)
    """
    db_path = Path(db_path)
    with open(db_path, "r+b") as f:
        data = f.read()
        name_bytes = obj_name.encode("ascii").ljust(0x60, b"\x00")
        start = data.find(name_bytes)
        if start == -1:
            return False
        f.seek(start + param_offset)
        f.write(new_value.to_bytes(4, "little"))
        return True

