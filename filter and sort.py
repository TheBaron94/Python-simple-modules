# LAB 6.13
# Adam Schmidt
# A program to sort a list in ascending order and remove negative numbers.

numbers = input()
list_numbers = numbers.split(' ')
list_int = []
list_nonneg = []
for i in list_numbers:
    list_int.append(int(i))
for i in list_int:
    if i >= 0:
        list_nonneg.append(i)

list_nonneg.sort()

for i in list_nonneg:
    print(i, end=' ')
