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
    name = input("Enter a name: ")
    age = input("Enter age: ")
    email = input("Enter an email address: ")
    new_dict["name"], new_dict["age"], new_dict["email"] = name, age, email
    contents.append(new_dict)

    new_text = json.dumps(contents)
    path.write_text(new_text)

if __name__ == "__main__":
    main()


