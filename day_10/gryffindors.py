students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}
print(*gryffindors, sep="\n")
print()

for i, student in enumerate(students):
    print(i + 1, student)
