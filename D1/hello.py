
def greet(name="User"):
    return f"Hello {name}"


def sum(*num):
    total = 0
    for i in num:
        total += i
    return total


def user(**details):
    for i in details:
        print(f"{details[i]}")


print("Jai Sree Ram")
name = "Raja"
print(name)
name = 3
print(name)
if (name == 3):
    print("yes")

names = ["Kumar", "Kiran", "Krishna", f"{name}"]
print(names)
for na in names:
    print(greet(na))

print(greet())
print(sum(10, 20, 30))
print((30, 40)[0])
user(name="JJ", age=34)
