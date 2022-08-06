# LAB 6.12
# Adam Schmidt
# a program to find the average and max of input

# Get in put from user and turn into int list.
numbers = input()
list_numbers = numbers.split(' ')
list_int = []
for i in list_numbers:
    list_int.append(int(i))

# Find max and average
avg_num = sum(list_int) // len(list_int)
max_num = max(list_int)

# Return result
print(avg_num)
print(max_num)


