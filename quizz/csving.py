import re
import random

path = "quizz\\untidycapitals.txt"

with open(path, "r") as f:
    text = f.read()

blud = re.compile(r'[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{4,105}?|[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{0,105}?|[A-Za-z]{4,150}')
geo_list = blud.findall(text)

states_dict = {}

state, capital = 0, 1

while state <= 98 and capital <= 100:
    states_dict[geo_list[state]] = geo_list[capital]
    state += 2
    capital += 2

states = [key for key in states_dict.keys()]

questions = []

for i in range(50):
    question = f"What is the capital of {states[i]}?"
    questions.append(question)









