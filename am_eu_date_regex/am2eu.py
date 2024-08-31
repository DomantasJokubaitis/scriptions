import re, os
from pathlib import Path


path = Path("am_eu_date_regex")
file_paths = os.listdir(path)
regex = re.compile(r"\d{2}-\d{2}-\d{4}")

def main():
    """finds mm-dd-yyyy in a filename and switches it up for the dd-mm-yyyy format"""

    for item in file_paths:
        answer = regex.search(item)

        if answer:
            am_date = answer.group()

            full_old_path = os.path.join(path, item)

            am_date_list = am_date.split("-")

            if am_date_list[0] == am_date_list[1] or int(am_date_list[0]) > 12:
                continue

            mm, dd = am_date_list[0], am_date_list[1]
            eu_date = f"{dd}-{mm}-{am_date_list[2]}"
            
            new_filename = item.replace(am_date, eu_date)
            full_new_path = os.path.join(path, new_filename)
            os.rename(full_old_path, full_new_path)

            print(f"Renamed {full_old_path} to {full_new_path}")


if __name__ == "__main__":
    main()
