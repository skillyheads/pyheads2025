import math
number = int(input("Enter a number"))
is_prime = True
for i in range(2, math.sqrt(number)):
    if (number != 2 and number % i == 0):
        is_prime = False
        break

print(is_prime)
