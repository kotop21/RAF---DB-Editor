from colorama import init, Fore, Style
from construct import Struct, Int32ul, PaddedString

from services.read_objects import read_objects

init(autoreset=True)

ObjectEntry = Struct(
    "name" / PaddedString(0x60, "ascii"),  
    "hp" / Int32ul                          
)

if __name__ == "__main__":
    objects = read_objects("dbobjects.dat")
    
    for obj_id, name, hp in objects:
        print(f"{Fore.CYAN}[ID {obj_id}]{Style.RESET_ALL} {Fore.YELLOW}{name}{Style.RESET_ALL} — HP: {Fore.RED}{hp}{Style.RESET_ALL}")
