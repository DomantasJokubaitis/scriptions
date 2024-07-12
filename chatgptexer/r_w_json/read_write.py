import json
from pathlib import Path

path = Path("chatgptexer\\r_w_json\\data.json")

def loading():
    if path.exists():
        try:
            read = path.read_text()
            contents = json.loads(read)
            return contents
        except FileNotFoundError:
            print("File not found. ")
            return []
        except json.JSONDecodeError:
            print("Decoding failed. ")
            return []
    if not path.exists():
        print("Path doesn't exist!")
        return []
    

def main():
    contents = loading()

    if contents == None:
        contents = []
        
    new_dict = {}
    commands = ("add", "search", "modify", "delete")
    wish = input("Add | Search | Modify | Delete :").lower()
    while wish not in commands:
        wish = input("Unknown command, try again: ")
    if "add" in wish:
        name = str(input("Enter a name: "))
        age = int(input("Enter age: "))
        email = input("Enter an email address: ")
        while "@" not in email:
            email = input("Invalid email, try again: ")
        new_dict["name"], new_dict["age"], new_dict["email"] = name, age, email
        contents.append(new_dict)
    """elif "modify" in wish:
        change_person = input("Enter the person's name to modify: ")
        for dictionary in contents:
            if dictionary[change_person]:
                #user should be able to enter what info to modify, like only age or age and mail
    """
    new_text = json.dumps(contents)
    path.write_text(new_text)

if __name__ == "__main__":
    main()

#implement search function by name
#implement delete function by name
#implement detail update function 


