num = int(input("enter the number to calculate: "))

if num < 0:
    print("Provide Valid Input")
elif num == 0 or num == 1:
    print('1')
else:
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    print(fact)
