import webbrowser, sys

args = sys.argv
if len(args) > 2:
    pass
else:
    print("Address too short")
    sys.exit()
google_maps = "https://www.google.com/maps/place/"

new_address = ("+".join(args[1:])).replace(",", "")

full_url = google_maps+new_address
webbrowser.open(full_url)
