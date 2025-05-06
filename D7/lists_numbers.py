# find min and max
ages = [30, 40, 24, 8, 67, 89, 32, 56, 78, 9]
min = ages[0]
for age in ages:
    if (min > age):
        min = age
print(f"Minimum number in the list is {min}")

max = ages[0]
for age in ages:
    if (max < age):
        max = age
print(f"Maximum number in the list is {max}")

min = ages[0]
max = ages[0]
for age in ages:
    if (min > age):
        min = age
    if (max < age):
        max = age
print(f"Minimum number is {min} maximum number is {max}")
