from pathlib import Path
from colorama import init, Fore, Style
from readchar import readkey, key

from services.backup_file import backup_file
from services.dat_json import dat_to_json_generic, json_to_dat_generic
from config import DB_FOLDER

SCHEMAS_FOLDER = Path("schemas")
init(autoreset=True)


def list_pairs():
    dat_files = list(DB_FOLDER.glob("*.dat"))
    pairs = []
    for dat in dat_files:
        schema = SCHEMAS_FOLDER / (dat.stem + ".json")
        if schema.exists():
            pairs.append((dat, schema))
    return pairs


def main():
    pairs = list_pairs()
    if not pairs:
        print(Fore.RED + "❌ No matching .dat and schema files found!" + Style.RESET_ALL)
        return

    for dat, _ in pairs:
        backup_file(dat)

    options = [
        "Export all .dat → .json",
        "Apply all .json → .dat",
        "Exit"
    ]
    selected = 0

    try:
        while True:
            print("\033c", end="")
            print(Fore.MAGENTA + "\nWhat do you want to do?" + Style.RESET_ALL)

            for i, option in enumerate(options):
                prefix = "> " if i == selected else "  "
                option_color = Fore.CYAN if i == selected else ""
                print(f"{option_color}{prefix}[{i+1}] {option}{Style.RESET_ALL}")

            k = readkey()
            choice = None
            if k == key.UP:
                selected = (selected - 1) % len(options)
            elif k == key.DOWN:
                selected = (selected + 1) % len(options)
            elif k == key.ENTER:
                choice = selected
            elif k in ["1", "2", "3"]:
                choice = int(k) - 1

            if choice == 0:
                for dat, schema in pairs:
                    dat_to_json_generic(dat, schema)
                input(Fore.CYAN + "\n✅ Export done. Press Enter..." + Style.RESET_ALL)
            elif choice == 1:
                for dat, schema in pairs:
                    json_to_dat_generic(dat, schema)
                input(Fore.CYAN + "\n✅ Changes applied. Press Enter..." + Style.RESET_ALL)
            elif choice == 2:
                print(Fore.CYAN + "👋 Exiting..." + Style.RESET_ALL)
                break

    except KeyboardInterrupt:
        print(Fore.CYAN + "\n👋 Exiting..." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
