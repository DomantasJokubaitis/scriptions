import re
import random
import os

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

states, capitals = [key for key in states_dict.keys()], [value for value in states_dict.values()]

def logic():

    question_number = 1
    control = list(range(50))

    while control:
        number = random.choice(control)
        control.remove(number)
        question = f"{question_number}. What is the capital of {states[number]}?"
        answers = []
        answer = capitals[number]
        answers.append(answer)
        fake_ans_choices = (list(range(50)))

        i = 3
        while i > 0:
            fake_ans_num = random.choice(fake_ans_choices)
            fake_ans_choices.remove(fake_ans_num)
            fake_answer = capitals[fake_ans_num]
            answers.append(fake_answer)
            i -= 1
        random.shuffle(answers)


        answer_choices = ["A", "B", "C", "D"]
        answer_number = 0
        for a in answers:
            print(f"{answer_choices[answer_number]}. {a}")
            answer_number += 1
        question_number += 1

path2 = "quizz\\"
for i in range(1, 36):
    filename = f"number{i}"
    new = os.path.join(path, filename + ".txt")
    logic()
    with open(new, "w") as n:
        n.write()













