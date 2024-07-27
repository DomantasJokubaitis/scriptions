### program which extracts US's states and capitals from a text file using regex and makes 35 random quizes with 50 random questions each

import re, random, os
from pathlib import Path

file_path = Path("untidycapitals.txt")

with open(file_path, "r") as f:
    text = f.read()

regex = re.compile(r'\S[a-zA-Z]+\s?[a-zA-Z]+\s?[A-Za-z]+?\b')
states_capitals_list = regex.findall(text)

states, capitals = [], []

for s in range(0, 99, 2):
    states.append(states_capitals_list[s])

for c in range(1, 100, 2):
    capitals.append(states_capitals_list[c]) 

def logic() -> list:

    quiz, question_number, control = [], 1, list(range(50))

    while control:

        # makes a random question, appends true answer to an answer list
        number: int = random.choice(control)
        control.remove(number)
        question: str = f"{question_number}. What is the capital of {states[number]}?"
        quiz.append(question)
        answers = []
        answers.append(capitals[number])

        # chooses three random untrue answers from leftover states, appends them to an answer list, shuffles it
        answers_fill = list(range(50))
        answers_fill.remove(number)
        fake_ans_num: list = random.sample(answers_fill, 3)
        for o in fake_ans_num:  
            answers.append(capitals[o])
        random.shuffle(answers)

        # makes formatted answers and appends them to the quiz
        answer_choices = iter(["A", "B", "C", "D"])
        for a in answers:
            format_answer = (f"{next(answer_choices)}. {a}")
            quiz.append(format_answer)

        question_number += 1
    return quiz

def main():
    
    quiz_dir = Path("generated_quizes")
    quiz_dir.mkdir(parents=True, exist_ok=True)

    target = int(input("How many quizes would you like prepared? "))
    for i in range(1, target+1):
        filename = f"quiz_number{i}.txt"
        new_filename = (quiz_dir / filename)
        quiz: list = logic()
        with open(new_filename, "w") as n:
            for item in quiz:
                n.write(f"{item}\n")
            
if __name__ == "__main__":
    main()












