# Design and implement a Python program that is based on the
# following requirements: a) program will find all numbers which are divisible
# by 7 but are not a multiple of 5; and
# b) numbers between 2000 and 3200.

def sevensnotfives(num1 = 2000, num2 = 3200):
    my_list = []
    for i in range(num1,num2 + 1):
        if (i % 7 == 0):
            if (i % 5 != 0):
                my_list.append(i)
    print(my_list)

sevensnotfives()
