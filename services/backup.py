from pathlib import Path
import shutil
from colorama import Fore, Style

def backup_file(file_path):
    """
    Creates a backup of the binary file with the .bac extension, if it does not already exist.
    """
    file_path = Path(file_path)
    backup_path = file_path.with_suffix(file_path.suffix + ".bac")
    if backup_path.exists():
        print(Fore.YELLOW + f"Бэкап уже существует: {backup_path}{Style.RESET_ALL}")
    else:
        shutil.copy(file_path, backup_path)
        print(Fore.GREEN + f"Бэкап создан: {backup_path}{Style.RESET_ALL}")
    return backup_path
