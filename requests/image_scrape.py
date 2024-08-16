import requests, webbrowser, sys
from bs4 import BeautifulSoup

res = requests.get('https://www.lrt.lt/')
res.raise_for_status()

soup = BeautifulSoup(res.content, "html.parser")
elems = soup.find_all("img", class_ = "media-block__image")

i: int = int(sys.argv[1])

for elem in elems:
    link = elem.get("data-src")
    webbrowser.open(f"https://www.lrt.lt/{link}")
    i -= 1
    if i == 0:
        break
