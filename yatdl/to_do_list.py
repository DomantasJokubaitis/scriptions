from pathlib import Path
import json

dir_path = Path("yatdl")
file_path = dir_path / "info.json"
dir_path.mkdir(parents=True, exist_ok=True)

def save_json():
    """Saves contents to a JSON file"""

    with open(file_path, "w") as f:
        json.dump(info, f)

def load_json():
    """Loads json file from the file path"""

    try:
        content = file_path.read_text()
        info = json.loads(content)
        return info
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


if not file_path.exists():
    info = {}
    save_json()
else:
    info = load_json()

def welcome():
    """Welcomes user by their name or asks for their name if it isn't known """

    try:
        print(f"Welcome back, {info['name']}")
    except KeyError:
        name = str(input("Welcome to the program, what is your name?\n"))
        info['name'] = name
        save_json()

    
def difficulty(x):
    """Sets a difficulty for a specific task"""
    while True:
        try:
            task_difficulty = int(input("Task difficulty 1-3: "))
            if 1 <= task_difficulty <= 3:
                info[x] = task_difficulty
                save_json()
                print("Task succesfully saved! ")
                break
            else:
                print("Difficulty level not valid! ")
        except ValueError:
            continue

def new_task():
    """Asks for a task name from user and calls the difficulty function"""

    while True:
        task_name = input("New task: ")
        if task_name in info:
            print("Task already exists! ")
        else:
            break
    difficulty(task_name)


def list_tasks():
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

def modify_task():
    """User modifies an already existing task"""

    task = input("Task to modify: ")
    if task in info.keys():
        task_name = input("Rename task: ")
        info[task_name] = info.pop(task)
        difficulty(task_name)
    else:
        print("Task doesn't exist! ")

def main():
    """Acts as a menu"""

    welcome()
    while True:
        choice = input("New task / List tasks / Modify /  Exit: ").lower()
        if choice == "new" or choice == "new task":
            new_task()
        elif choice == "list" or choice == "list tasks":
            list_tasks()
        elif choice == "modify":
            modify_task()
        elif choice == "exit":
            print("Exiting...")
            break
        else:
            print(f"Command unknown\n")


if __name__ == "__main__":
    main()

