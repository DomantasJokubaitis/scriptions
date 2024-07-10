### program which extracts US's states and capitals from a text file using regex and makes 35 random quizes with 50 random questions each

import re
import random
import os

path1 = "quizz\\untidycapitals.txt"

with open(path1, "r") as f:
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
    whole_question = []

    while control:
        number = random.choice(control)
        control.remove(number)
        question = f"{question_number}. What is the capital of {states[number]}?"
        whole_question.append(question)
        answers = []
        answer = capitals[number]
        answers.append(answer)

        fake_ans_choices = (list(range(50)))
        fake_ans_choices.remove(number)
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
            format_answer = (f"{answer_choices[answer_number]}. {a}")
            whole_question.append(format_answer)
            answer_number += 1
        question_number += 1
    return whole_question

logic()


path2 = "quizz\\"
for i in range(1, 36):
    filename = f"quiz_number{i}"
    new = os.path.join(path2, filename + ".txt")
    quiz = logic()
    with open(new, "w") as n:
        for item in quiz:
            n.write(f"{item}\n")















