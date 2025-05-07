def fact(number):
    if number > 1:
        return number * fact(number - 1)
    else:
        return number


number = int(input("Enter the  number"))
result = fact(number)
print(result)
