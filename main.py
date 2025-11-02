from colorama import init, Fore, Style
from services.backup import backup_file
from services.read_objects import read_objects
from services.save_objects_json import save_objects_json
from services.binary_utils import update_object_param
from
import json
from pathlib import Path

init(autoreset=True)

DB_PATH = "dbobjects.dat"
JSON_PATH = "objects.json"
HP_OFFSET = 0x78


def dat_to_json():
    print(Fore.CYAN + "\n📦 Converting dbobjects.dat → objects.json..." + Style.RESET_ALL)
    objects = read_objects(DB_PATH)
    save_objects_json(objects, JSON_PATH)
    print(Fore.GREEN + f"✅ Successfully exported to {JSON_PATH}" + Style.RESET_ALL)


def json_to_dat():
    print(Fore.CYAN + "\n🔄 Applying changes from JSON to dat..." + Style.RESET_ALL)

    json_path = Path(JSON_PATH)
    if not json_path.exists():
        print(Fore.RED + f"❌ File {JSON_PATH} not found!" + Style.RESET_ALL)
        return

    with open(json_path, "r", encoding="utf-8") as f:
        objects = json.load(f)

    updated = 0
    for obj in objects:
        name = obj.get("name")
        hp = obj.get("hp")

        if not name or not isinstance(hp, int):
            continue

        if update_object_param(DB_PATH, name, HP_OFFSET, hp):
            updated += 1
        else:
            print(Fore.RED + f"❌ Object with name '{name}' not found in binary file!" + Style.RESET_ALL)

    print(Fore.GREEN + f"✅ Successfully applied changes: {updated}" + Style.RESET_ALL)


def main():
    backup_file(DB_PATH)
    while True:
        print(Fore.MAGENTA + "\nWhat do you want to do?" + Style.RESET_ALL)
        print("1. dat file → json file")
        print("2. json file → dat file")
        print("3. exit")

        choice = input(Fore.YELLOW + "\nYour choice: " + Style.RESET_ALL).strip()
        if choice == "1":
            dat_to_json()
            break
        elif choice == "2":
            json_to_dat()
            break
        elif choice == "3":
            print(Fore.CYAN + "👋 Exiting the program." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ Invalid choice, please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
