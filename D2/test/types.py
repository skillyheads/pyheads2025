""" # id = 1
name = "Kumar"
age = 23
height = 5.9
# int, float, boolean, string, list, tuple, set, dict
# Student name is kumar and hid age is 23
print(f"Student name is {name} and his age is {age}")
new_name = "Kumar"
slogan = "All indians are by brothers and sisters"
print('-'.join(slogan.split()))
marks = [85, 89, 56, 78, 90, 57]
print(id(marks))

marks[2] = 75
print(id(marks))
print(marks[-2:])

marks.extend([99, 98])
print(marks[::-1])
del marks[2]
print(marks)
marks.sort(reverse=True)
print(marks.pop())
print(marks)

student = (1, "Kumar", 23, 5.9)
std_id, name, age, height = student
print(height) """

""" 
s1 = "satya"
s2 = "ravi"
s2 = s1
print(id(s1) is id(s2))

s1 = "kumar"
s2 = "kumar"
print(id(s1) is id(s2))
 """

s1 = "satya"
s2 = "ravi"
s2 = s1
print(id(s1) is id(s2))

s1 = "satya"
s2 = "ravi"
s2 = s1[:]
print(id(s1) is id(s2))
