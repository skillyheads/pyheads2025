students = {1: "Kumar", 2: "Geetha", 3: "Praveen"}
students[2] = "Raja"

print(students.items())

for key in students:
    print(students[key])

print((2, "Raja") in students.items())

del students[2]
print(students)
batches_list = [["btech", 30], ["mca", 20]]
batches = dict(batches_list)
print(batches)
batches = dict.fromkeys(["btech", "mca"], 1)
print(batches)

batches_list = ["btech", "mca"]
batches_strength = [30, 20]
batches = dict(zip(batches_list, batches_strength))
print(batches)
