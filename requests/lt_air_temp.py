import requests, bs4, webbrowser, unicodedata

# ask user for input(a city/town in Lithuania)
def temp_lookup(city) -> str:
    unicode_city: str = unicodedata.normalize("NFD", city).encode("ascii", "ignore").decode("ascii").lower()
    website = f"https://www.meteo.lt/?area={unicode_city}" 
    raw_data = requests.get(website)
    raw_data.raise_for_status()

    soup_object = bs4.BeautifulSoup(raw_data.text, "html.parser")
    elems = soup_object.select("span")
    temp = elems[10].getText().strip()
    return temp

def main():
    city: str = input("Enter a location in Lithuania to look up the temperature: ")
    temp = temp_lookup(city)
    print(f"It's {temp} outside in {city}.")

if __name__ == "__main__":
    main()
