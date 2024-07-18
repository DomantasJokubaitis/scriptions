### program which extracts US's states and capitals from a text file using regex and makes 35 random quizes with 50 random questions each

import re
import random
import os

path1 = "quizz\\untidycapitals.txt"

with open(path1, "r") as f:
    text = f.read()

regex = re.compile(r'[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{4,105}?|[a-zA-Z]{2,100}\s[a-zA-Z]{2,150}\s?[A-Za-z]{0,105}?|[A-Za-z]{4,150}')
states_capitals_list = regex.findall(text)

states_dict = {}

state, capital = 0, 1

while state <= 98 and capital <= 100:
    states_dict[states_capitals_list[state]] = states_capitals_list[capital]
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
        answers.append(capitals[number])


        #chooses three random untrue answers from leftover states
        fake_ans_choices = (list(range(50)))
        fake_ans_choices.remove(number)
        for i in range(3):
            fake_ans_num = random.choice(fake_ans_choices)  
            fake_ans_choices.remove(fake_ans_num)
            answers.append(capitals[fake_ans_num])
        random.shuffle(answers)

        answer_choices = ["A", "B", "C", "D"]
        answer_number = 0
        for a in answers:
            format_answer = (f"{answer_choices[answer_number]}. {a}")
            whole_question.append(format_answer)
            answer_number += 1
        question_number += 1
    return whole_question


def main():

    path2 = "quizz\\"
    target = int(input("How many quizes would you like prepared? "))
    for i in range(1, target+1):
        filename = f"quiz_number{i}"
        new = os.path.join(path2, filename + ".txt")
        quiz = logic()
        with open(new, "w") as n:
            for item in quiz:
                n.write(f"{item}\n")
            
if __name__ == "__main__":
    main()















