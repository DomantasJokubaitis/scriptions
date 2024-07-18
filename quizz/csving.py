### program which extracts US's states and capitals from a text file using regex and makes 35 random quizes with 50 random questions each

import re
import random
import os

path1 = "quizz\\untidycapitals.txt"

with open(path1, "r") as f:
    text = f.read()

regex = re.compile(r'\S[a-zA-Z]+\s?[a-zA-Z]+\s?[A-Za-z]+?\b')
states_capitals_list = regex.findall(text)

states, capitals = [], []

for s in range(0, 99, 2):
    states.append(states_capitals_list[s])

for c in range(1, 100, 2):
    capitals.append(states_capitals_list[c]) 

def logic():

    quiz, question_number, control = [], 1, list(range(50))

    while control:

        # makes a random question, appends true answer to an answer list
        number = random.choice(control)
        control.remove(number)
        question = f"{question_number}. What is the capital of {states[number]}?"
        quiz.append(question)
        answers = []
        answers.append(capitals[number])

        # chooses three random untrue answers from leftover states, appends them to an answer list, shuffles it
        answers_fill = list(range(50))
        answers_fill.remove(number)
        for _ in range(3):
            fake_ans_num = random.choice(answers_fill)  
            answers_fill.remove(fake_ans_num)
            answers.append(capitals[fake_ans_num])
        random.shuffle(answers)

        # makes formatted answers and appends them to the quiz
        answer_choices, answer_number = ["A", "B", "C", "D"], 0
        for a in answers:
            format_answer = (f"{answer_choices[answer_number]}. {a}")
            quiz.append(format_answer)
            answer_number += 1
        question_number += 1
    return quiz


def main():

    path2 = "quizz\\"
    target = int(input("How many quizes would you like prepared? "))
    for i in range(1, target+1):
        filename = f"quiz_number{i}"
        new_filename = os.path.join(path2, filename + ".txt")
        quiz = logic()
        with open(new_filename, "w") as n:
            for item in quiz:
                n.write(f"{item}\n")
            
if __name__ == "__main__":
    main()















