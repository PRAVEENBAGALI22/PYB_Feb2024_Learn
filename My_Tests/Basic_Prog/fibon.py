num = int(input("Provide a number: "))

a = 0
b = 1


if num < 0:
    print("Provide Valid Input")
elif num == 1 :
    print(a + b)
else:
    for i in range(2,num):
        c = a + b
        a = b
        b = c
        print(c, end=' ')

