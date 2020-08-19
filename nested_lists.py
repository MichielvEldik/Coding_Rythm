"""
Nested Lists.

Given the names and grades for each students in class of N students.
Store them in a nested list and print name(s) having the second lowest grade.
"""

python_students = [['Harry', 37.21],
                   ['Berry', 37.21],
                   ['Tina', 37.2],
                   ['Akriti', 41],
                   ['Harsh', 39]]

initial = ['', 100]


def find_worst_grade(worst_grade, python_students):
    index = 0
    for count, i in enumerate(python_students):
        if i[1] < worst_grade[1]:
            worst_grade[1] = i[1]
            worst_grade[0] = i[0]
            index = count
    new_students = python_students.pop(index)

    return new_students, python_students


worst_grade, new_students = find_worst_grade(initial, python_students)
print(worst_grade, new_students)
second_worst, newer_students = find_worst_grade(worst_grade, new_students)
print(second_worst, new_students)
