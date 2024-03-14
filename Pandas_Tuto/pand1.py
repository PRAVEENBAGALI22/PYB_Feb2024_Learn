import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

a = [1, 7, 2]

myvar1 = pandas.Series(a)

print(myvar1)


a = [1, 7, 2]

myvar2 = pandas.Series(a, index = ["x", "y", "z"])

print(myvar2)


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar3 = pd.Series(calories)

print(myvar3)

