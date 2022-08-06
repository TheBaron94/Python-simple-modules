# 3.11 Lab
# Adam Schmidt
# a program to find the smallest of 3 given numbers

# get numbers from user
num_one = int(input())
num_two = int(input())
num_three = int(input())

if (num_one < num_two) and (num_one < num_three):
    print(num_one)
elif num_two < num_three:
    print(num_two)
else:
    print(num_three)
