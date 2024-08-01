import requests

website = requests.get("https://roadmap.sh/linux")
website.raise_for_status()
with open("website_hd.txt", "wb") as w:
    for chunk in website.iter_content(100000):
        w.write(chunk)
