import json
from pathlib import Path
from colorama import Fore, Style
from tqdm import tqdm

from services.save_objects_json import save_objects_json
from config import DB_PATH, JSON_SUFFIX, UNPACK_FOLDER


def dat_to_json(dat_file, read_func, data):
    UNPACK_FOLDER.mkdir(parents=True, exist_ok=True)
    json_file = UNPACK_FOLDER / (Path(dat_file).stem + JSON_SUFFIX)

    print(Fore.CYAN + f"\n📦 Converting {dat_file} → {json_file}..." + Style.RESET_ALL)
    save_objects_json(data, dat_file)
    print(Fore.GREEN + f"✅ Successfully exported to {json_file}" + Style.RESET_ALL)
