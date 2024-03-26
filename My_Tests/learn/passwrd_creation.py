import random
import string

length = int(input("Enter the length of password to be created : "))
print('''
      '1 : Numerical'
      '2: ascii'
      '3: punctuation '
      '4: exit''')

charters_lst = ""
while True:
    choice = int(input("Enter the Number : "))
    if choice == 1:
        charters_lst = charters_lst + string.digits
    elif choice == 2:
        charters_lst = charters_lst + string.ascii_letters
    elif choice == 3:
        charters_lst = charters_lst + string.punctuation
    elif choice == 4:
        break
    else:
        print("Provide valid input ")

password = []

for i in range(length):
    randmchar = random.choice(charters_lst)
    password.append(randmchar)

print("".join(password))
