
def may_length(name):
    if (len(name) > 5):
        return len(name)
    else:
        return 5


def capitalize_names(names):
    print(id(names))
    for i in range(len(names)):
        names[i] = names[i].upper()


def var_args(age, **args):
    print(type(args))
    print(args["seetha"])


var_args(10, seetha=20, geetha=30, name="40")

names = ["Bhagath", "Laal", "Baal", "Paal", "Savarkar", "Bose"]
print(id(names))
capitalize_names(names)
print(names)

ages = []
ages = [age ** 3 for age in range(2, 10, 2)]
print(ages)

lengths = dict([[name, len(name)] for name in names if len(name) > 4])
print(lengths)

lengths = dict([[name, may_length(name)] for name in names])
print(lengths)

lengths = dict([[name, len(name)] if len(name) > 4 else [name, 5]
               for name in names])
print(lengths)

s1 = 'Abc'
s2 = 'XYz'
[ch1 + ch2 for ch1 in s1 for ch2 in s2]
[ch1 + ch2 for ch1 in s1 if ch1.islower() for
 ch2 in s2 if ch2.isupper()]


students = {'12AB': {'name': 'Raj', 'class': 5,
                     'marks': 400},
            '14XD': {'name': 'Dev', 'class': 6,
                     'marks': 350},
            '12YR': {'name': 'Rob', 'class': 4,
                     'marks ': 289},
            '13CP': {'name': 'Zen', 'class': 5,
                     'marks': 315},
            '23CX': {'name': 'Ted', 'class': 5,
                     'marks': 270},
            '15XG': {'name': 'Sam', 'class': 3,
                     'marks': 390},
            '19HY': {'name': 'Pam', 'class': 5,
                     'marks': 250},
            }
names = {id: record.get("marks") for id,
         record in students.items()}

print(names)

slogan = "My name is Godse"
counts = {ch: slogan.count(ch) for ch in slogan}
print(counts)
