from colorama import init, Fore, Style
from services.backup import backup_file
from services.json_utils import load_objects_json, save_objects_json
from services.binary_utils import update_object_param

init(autoreset=True)

HP_OFFSET = 0x78

def edit_object(db_path, json_path):
    backup_file(db_path)
    objects = load_objects_json(json_path)

    print(Fore.CYAN + "🐟 Welcome to the Object Editor! 🐟" + Style.RESET_ALL)

    while True:
        print("\n" + Fore.MAGENTA + "✨ Available objects to edit:" + Style.RESET_ALL)
        for o in objects:
            print(f"  {Fore.CYAN}[ID {o['id']}] {Fore.YELLOW}{o['name']}{Style.RESET_ALL}")
        print(Fore.YELLOW + "  0. Exit" + Style.RESET_ALL)

        obj_id = input("\nEnter the ID of the object to edit 🖊️ (0 - exit): ").strip()
        if not obj_id.isdigit():
            print(Fore.RED + "❌ Invalid ID, please try again!" + Style.RESET_ALL)
            continue
        obj_id = int(obj_id)
        if obj_id == 0:
            print(Fore.CYAN + "👋 Exiting the editor. Bye!" + Style.RESET_ALL)
            break

        obj = next((o for o in objects if o["id"] == obj_id), None)
        if not obj:
            print(Fore.RED + f"❌ Object with ID {obj_id} not found" + Style.RESET_ALL)
            continue

        while True:
            print("\n" + Fore.GREEN + "🛠 Object parameters:" + Style.RESET_ALL)
            print(f"{Fore.CYAN}ID: {obj['id']}{Style.RESET_ALL} (cannot edit)")
            print(f"{Fore.YELLOW}Name: {obj['name']}{Style.RESET_ALL} (cannot edit)")

            editable_params = [key for key in obj if key not in ("id", "name")]
            for i, key in enumerate(editable_params, start=1):
                print(f"  {i}. {key}: {Fore.RED}{obj[key]}{Style.RESET_ALL}")
            print(f"  0. Back 🔙")

            choice = input("\nEnter the number of the parameter to edit ✏️: ").strip()
            if not choice.isdigit() or int(choice) < 0 or int(choice) > len(editable_params):
                print(Fore.RED + "❌ Invalid choice, please try again!" + Style.RESET_ALL)
                continue

            choice = int(choice)
            if choice == 0:
                print(Fore.CYAN + "⬅️ Returning to object selection..." + Style.RESET_ALL)
                break

            param_to_change = editable_params[choice - 1]
            new_value = input(f"Enter new value for {param_to_change} 📝: ").strip()
            if not new_value.isdigit():
                print(Fore.RED + "❌ Only numbers are allowed!" + Style.RESET_ALL)
                continue
            new_value = int(new_value)

            obj[param_to_change] = new_value
            save_objects_json(objects, json_path)

            if param_to_change.lower() == "hp":
                success = update_object_param(db_path, obj["name"], HP_OFFSET, new_value)
                if success:
                    print(Fore.GREEN + f"💾 {param_to_change} successfully updated in binary!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "❌ Object not found in binary file" + Style.RESET_ALL)
