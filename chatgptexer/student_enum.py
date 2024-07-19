from statistics import mean

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
grades = [85, 92, 78, 90, 88]
average = mean(grades)

for index, (student, grade) in enumerate(zip(students, grades)):
    print(f"{index + 1}. {student} scored {grade} in their test")

print(f"\nAverage grade: {average}\n")

print("Students who scored above average:")
for student, grade in zip(students, grades):
    if grade > average:
        print(f"- {student}")

