batch_one = {'Kumar', 'Kumar', 'Raja'}
batch_two = {'Ramu', 'Seetha', 'Geetha'}

all_students = batch_one.union(batch_two)
print(all_students)
common_students = batch_one.intersection(batch_two)
print(common_students)
only_in_one = batch_one.difference(batch_two)
print(only_in_one)
not_in_common = batch_one.symmetric_difference(batch_two)
print(not_in_common)
print(batch_one.isdisjoint(batch_two))


ids = [10, 20, 30, 20, 30]
unique_ids = set(ids)
print(unique_ids)
