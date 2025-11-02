from colorama import init, Fore, Style
from construct import Struct, Int32ul, PaddedString
from services.read_objects import read_objects
from services.save_objects_json import save_objects_json
from services.edit_object import edit_object

init(autoreset=True)

ObjectEntry = Struct(
    "name" / PaddedString(0x60, "ascii"),
    "hp" / Int32ul
)

if __name__ == "__main__":
    objects = read_objects("dbobjects.dat")
    
    for obj_id, name, hp in objects:
        print(f"{Fore.CYAN}[ID {obj_id}]{Style.RESET_ALL} {Fore.YELLOW}{name}{Style.RESET_ALL} — HP: {Fore.RED}{hp}{Style.RESET_ALL}")
    
    json_path = save_objects_json(objects, "services/objects.json")
    edit_object("dbobjects.dat", "services/objects.json")
    # print(f"\n{Fore.GREEN}Данные сохранены в JSON: {json_path}{Style.RESET_ALL}")
