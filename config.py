from pathlib import Path

# Offsets for dbobjects.dat
HP_OFFSET = 0x78
DAMAGE_OFFSET = 0xC4

# Offsets for dbtechtree.dat
GOLD_OFFSET = 0x84
WOOD_OFFSET = 0x7C


# Files 
DB_FOLDER = Path("db")
DB_PATH = [DB_FOLDER / "dbobjects.dat", DB_FOLDER / "dbtechtree.dat"]
JSON_SUFFIX = ".json"

BACUP_FOLDER = Path("backup")

UNPACK_FOLDER = Path("unpack")
