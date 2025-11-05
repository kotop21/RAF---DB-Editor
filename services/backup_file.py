from pathlib import Path
import shutil
from colorama import Fore, Style
from config import BACUP_FOLDER

def backup_file(file_path):
    """
    Creates a backup of the binary file in BACUP_FOLDER with the .bac extension
    if it does not already exist.
    """
    file_path = Path(file_path)
    
    BACUP_FOLDER.mkdir(parents=True, exist_ok=True)
    
    backup_path = BACUP_FOLDER / (file_path.name + ".bac")
    
    if backup_path.exists():
        print(Fore.YELLOW + f"Backup already exists: {backup_path}" + Style.RESET_ALL)
    else:
        shutil.copy(file_path, backup_path)
        print(Fore.GREEN + f"Backup created: {backup_path}" + Style.RESET_ALL)
    
    return backup_path
