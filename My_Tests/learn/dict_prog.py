thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

for key, value in thisdict.items():
    print(key, value)

for val in thisdict.values():
    print(val)
    if val == "Mustang":
        break


for i in range(1,11):
    print (i)
    if i == 5:
        break
print("Condition met")

for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
