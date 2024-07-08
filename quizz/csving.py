import re

path = "quizz\\untidycapitals.txt"

with open(path, "r") as f:
    text = f.read()

blud = re.compile(r'[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{4,105}?|[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{0,105}?|[A-Za-z]{4,150}')
geo_list = blud.findall(text)

print(geo_list)

states_dict = {}

state, capital = 0, 1

while state <= 98 and capital <= 100:
    states_dict[geo_list[state]] = geo_list[capital]
    state += 2
    capital += 2

for key, value in states_dict.items():
    print(key, value)


