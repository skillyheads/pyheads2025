from copy import deepcopy

studends = {
    "ROL001": {
        "student_name": "Raja",
        "student_age": 23,
        "student_marks": [80, 89, 90, 76, 78, 98]
    },
    "ROL002": {
        "student_name": "Praveen",
        "student_age": 25,
        "student_marks": [89, 90, 90, 90, 65, 75]
    }
}

new_students = deepcopy(studends)

new_students["ROL002"]["student_age"] = 28

print(studends)
print(new_students)


new_students["ROL003"] = {
    "student_name": "Pradeep",
    "student_age": 29,
    "student_marks": [89, 90, 90, 90, 100, 100]
}

print(studends)
print(new_students)
