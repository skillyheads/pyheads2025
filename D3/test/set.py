from copy import *
rollnumbers = ["A001", "A002", "A003", "A002"]
rollnumbers.append("A004")
print(id(rollnumbers))
newrolls = rollnumbers.copy()
print(deepcopy(newrolls))
