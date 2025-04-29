def display(name1, name2, name3):
    print("Jai Hindh")
#    name = "Subhash"
    print(name)


def total(max_marks, *numbers):
    max_marks = 500
    total = 0
    for number in numbers:
        total += number
    print((total*100)/max_marks)


def total_marks(**marks_by_subjects):
    total = 0
    for number in marks_by_subjects.values():
        total += number
    print(total)


def display_names(students):
    for i in range(len(students)):
        students[i] = students[i].upper()
        print(students[i])


names_list = ["Subhash", "Bhagath", "Laal", "Baal", "Paal"]
display_names(names_list)
print(names_list)


total_marks(telugu=90, english=80, hindi=70, maths=100)

t_marks = 400
total(t_marks, 80, 90, 90, 95)
print(t_marks)
