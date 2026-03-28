students = ['Hermione', 'Harry', 'Ron']

for student in students:
    print(student)
print()

for i in range(len(students)):
    print(i + 1, students[i])

hogwarts_students = {
    'Hermione': 'Gryffindor',
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Draco': 'Slytherin'
}
print()

for student in hogwarts_students:
    print(student, hogwarts_students[student], sep=' -> ')
print()

students_data = [
    {'name': 'Hermione', 'home': 'Gryffindor', 'patronus': 'Otter'},
    {'name': 'Harry', 'home': 'Gryffindor', 'patronus': 'Stag'},
    {'name': 'Ron', 'home': 'Gryffindor', 'patronus': 'Jack Russell Terrier'},
    {'name': 'Draco', 'home': 'Slytherin', 'patronus': None},
]

for student in students_data:
    print(student['name'], student['home'], student['patronus'], sep=', ')
