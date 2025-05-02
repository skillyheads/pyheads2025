students = {}
names = ["Kumar", "Praveen", "Raja", "Ramesh", "Sumanth"]
for name in names:
    students[name] = len(name)
print(students)


students_comprehension = {name: len(name) for name in names}
print(students_comprehension)

students = {
    "R07CS001": {
        "name": "Bhagath",
        "marks": 100,
        "age": 23
    },
    "R07CS002": {
        "name": "Ajad",
        "marks": 98,
        "age": 23
    },
    "R07CS003": {
        "name": "Raju",
        "marks": 97,
        "age": 26
    },
    "R07CS004": {
        "name": "Bose",
        "marks": 100,
        "age": 54
    },
    "R07CS005": {
        "name": "Chandra Paal",
        "marks": 89,
        "age": 60
    },
    "R07CS005": {
        "name": "Seetha Rama Raju",
        "marks": 89,
        "age": 26
    }
}

student_marks = {}
for student in students.values():
    student_marks[student.get("name")] = student.get("marks")

print(student_marks)

student_marks = {}
for id, student in students.items():
    student_marks[id] = student.get("marks")

print(student_marks)

student_marks_2 = {id: 'A+' if student["marks"] == 100 else 'A'
                   for id, student in students.items()}
print(student_marks_2)
