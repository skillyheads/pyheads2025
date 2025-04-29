even_numbers = []
for num in range(50):
    if (num % 2 == 0):
        even_numbers.append(num)

print(even_numbers)

even_numbers = {num: num**2 for num in range(50) if num % 2 == 0}
print(even_numbers)
