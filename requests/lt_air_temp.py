import requests, bs4, unicodedata, sys


def temp_lookup(city: str) -> str:
    """get's the outside temperature of a city in Lithuania"""

    unicode_city = unicodedata.normalize("NFD", city).encode("ascii", "ignore").decode("ascii").lower()
    website = f"https://www.meteo.lt/?area={unicode_city}" 
    raw_data = requests.get(website, params = {"city" : unicode_city})
    raw_data.raise_for_status()

    soup_object = bs4.BeautifulSoup(raw_data.text, "html.parser")
    elems = soup_object.select("span")
    temp = elems[10].getText().strip()
    return temp

def main():
    city: str = sys.argv[1]
    temp = temp_lookup(city)
    print(f"It's {temp} outside in {city}.")

if __name__ == "__main__":
    main()

# need to add dashed between multiple city names,
# should handle incorrect city names somehow.
