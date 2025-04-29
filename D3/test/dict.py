total_marks_by_name = {"Kumar": 500, "": 250, "Krishna": 250}
print(total_marks_by_name.keys())

list1 = [['a', 1], ['b', 2], ['c', 3]]
d1 = dict(list1)


t1 = (('x', 4), ('y', 5), ('z', 6))
d2 = dict(t1)
print(d2)

stationery = ['pencil', 'marker', 'eraser', 'sharpener']
prices = dict.fromkeys(stationery, 1)
print(prices)

nested_dictionary = {
    "name": {
        "Kumar": "5"
    }
}

print(nested_dictionary)
