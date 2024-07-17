import re
from pathlib import Path

path = Path(r"pattern/phones.txt")
with open(path, "r") as f:
    text = f.read()

def main():

    phone_num_regex = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    answer = phone_num_regex.findall(text)
    print(answer)

if __name__ == "__main__":
    main()