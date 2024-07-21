from pathlib import Path
import json

dir_path = Path("yatdl")
file_path = dir_path / "info.json"
dir_path.mkdir(parents=True, exist_ok=True)

def save_json():
    with open(file_path, "w") as f:
        json.dump(info, f)

if not file_path.exists():
    info = {}
    save_json()
else:
    content = file_path.read_text()
    info = json.loads(content)


def welcome():
    try:
        print(f"Welcome back, {info["name"]}")
    except KeyError:
        name = str(input("Welcome to the program, what is your name?\n"))
        info["name"] = name
        save_json()

def new_task():
    while True:
        task_name = input("New task: ")
        if task_name in info.keys():
            print("Task already exists! ")
            continue
        else:
            break
    
    while True:
        try:
            task_difficulty = int(input("Task difficulty 1-3: "))
            if 1 <= task_difficulty <= 3:
                info[task_name] = task_difficulty
                save_json()
                print("Task succesfully saved! ")
                break
            else:
                print("Difficulty level not valid! ")
                continue
        except ValueError:
            continue

welcome()
new_task()