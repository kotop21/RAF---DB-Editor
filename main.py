from pathlib import Path
from colorama import init, Fore, Style
from readchar import readkey, key

from services.backup_file import backup_file
from services.binary_utils import update_object_param
from services.dat_json import dat_to_json, json_to_dat
from config import DB_PATH

init(autoreset=True)

def main():
    backup_file(DB_PATH)

    options = ["dat file → json file", "json file → dat file", "Exit"]
    selected = 0

    try:
        while True:
            print("\033c", end="")  
            print(Fore.MAGENTA + "\nWhat do you want to do?" + Style.RESET_ALL)

            for i, option in enumerate(options):
                prefix = "> " if i == selected else "  "
                option_color = Fore.CYAN if i == selected else ""
                number_color = Fore.BLUE + Style.BRIGHT
                print(f"{option_color}{prefix}{number_color}[{i+1}]{Style.RESET_ALL} {option_color}{option}{Style.RESET_ALL}")

            key_pressed = readkey()
            choice = None

            if key_pressed == key.UP:
                selected = (selected - 1) % len(options)
            elif key_pressed == key.DOWN:
                selected = (selected + 1) % len(options)
            elif key_pressed == key.ENTER:
                choice = selected
            elif key_pressed in ["1", "2", "3"]:
                choice = int(key_pressed) - 1
            else:
                continue

            if choice is not None:
                if choice == 0:
                    dat_to_json()
                    break
                elif choice == 1:
                    json_to_dat()
                    break
                elif choice == 2:
                    print(Fore.CYAN + "👋 Exiting the program." + Style.RESET_ALL)
                    break

    except KeyboardInterrupt:
        print(Fore.CYAN + "\n👋 Exiting the program." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
