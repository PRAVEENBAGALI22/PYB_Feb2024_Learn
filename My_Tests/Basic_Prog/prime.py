number_to_check = int(input("Enter the number to check for prime: "))

if number_to_check > 1:
    for i in range(2,number_to_check):
        if (number_to_check % i) == 0:
            print(number_to_check , "Its not a prime number")
            break
    else:
        print(number_to_check, "Its prime number")
else:
    print(number_to_check, "its not prime number which is less than 1")