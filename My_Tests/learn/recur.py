def adding_lst(lst):
    sum = 0

    for i in range(len(lst)):
        sum = sum + lst[i]

    return sum


adding_num = [1, 2, 3, 4, 5]
sum = adding_lst(adding_num)
print(sum)
