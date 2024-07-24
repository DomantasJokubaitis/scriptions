from pathlib import Path
import json

dir_path = Path("yatdl")
file_path = dir_path / "info.json"
dir_path.mkdir(parents=True, exist_ok=True)

def save_json(info: dict) -> None:
    """Saves contents to a JSON file"""

    with open(file_path, "w") as f:
        json.dump(info, f)

def load_json() -> dict:
    """Loads json file from the file path"""

    try:
        content = file_path.read_text()
        info = json.loads(content)
        return info
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


if not file_path.exists():
    info = {}
    save_json(info)
else:
    info: dict = load_json()

def welcome(info) -> None:
    """Welcomes user by their name or asks for their name if it isn't known """

    try:
        print(f"Welcome back, {info['name']}")
    except KeyError:
        name = str(input("Welcome to the program, what is your name?\n"))
        info['name'] = name
        save_json(info)

    
def set_difficulty(info: dict, task_name) -> None:
    """Sets a difficulty for a specific task"""
    while True:
        try:
            task_difficulty = int(input("Task difficulty 1-3: "))
            if 1 <= task_difficulty <= 3:
                info[task_name] = task_difficulty
                save_json(info)
                print("Task succesfully saved! ")
                break
            else:
                print("Difficulty level not valid, valid numbers are 1-3 ")
        except ValueError:
            print("Difficulty level not valid, valid numbers are 1-3 ")

def new_task(info: dict) -> None:
    """Asks for a task name from user and calls the difficulty function"""

    while True:
        task_name = input("New task: ")
        if task_name == "name":
            print("Task cannot be named 'name'! ")
        elif task_name in info:
            print("Task already exists! ")
        else:
            break
    set_difficulty(info, task_name)


def list_tasks(info: dict) -> None:
    """Lists tasks stored in the JSON file sorted and colored by difficulty"""

    diff1, diff2, diff3 = [], [], []
    difficulties = [diff1, diff2, diff3]

    # green, yellow, red in unicode
    colors = ["\u001b[32m", "\u001b[33m", "\u001b[31m"]

    for key in info.keys():
        if key == "name":
            continue
        elif info[key] == 1:
            diff1.append(key)
        elif info[key] == 2:
            diff2.append(key)
        elif info[key] == 3:
            diff3.append(key)

    for index, diff in enumerate(difficulties):
        print(f"\n{colors[index]}Difficulty {index + 1}")
        for item in diff:
            print(f"\t-{item}")

    # resets color to default
    print(f"\u001b[0m")

def modify_task(info: dict) ->  None:
    """User modifies an already existing task"""

    task = input("Task or name to modify: ")
    if task == "name":
        while True:
            name = input("Enter your new name: ")
            if name not in info:
                info["name"] = name
                save_json(info)
                print("Name succefully changed")
                break
            else:
                print("Name can't be the same as a task! ")
    elif task in info:
        task_name = input("Enter a new task name: ")
        info[task_name] = info.pop(task)
        set_difficulty(info, task_name)
    else:
        print("Task doesn't exist! ")

def delete_task(info: dict) -> None:
    """Deletes task from dictionary"""

    while True:

        task = input("What task would you like to remove? ")
        if task == "name":
            print("To change your name, select modify from the menu and enter 'name'. ")
        elif task in info:
            del info[task]
            save_json(info)
            print("Task succesfully deleted! ")
            break
        else:
            print("No such task exists")

def main(info: dict):
    """Acts as a menu"""

    welcome(info)
    while True:
        choice: str = input("New task / List tasks / Modify / Delete / Exit: ").lower()
        if choice == "new" or choice == "new task":
            new_task(info)
        elif choice == "list" or choice == "list tasks":
            list_tasks(info)
        elif choice == "modify":
            modify_task(info)
        elif choice == "delete":
            delete_task(info)
        elif choice == "exit":
            print("Exiting...")
            break
        else:
            print("Command unknown")


if __name__ == "__main__":
    main(info)

