# 3.12 Lab
# Adam Schmidt
# A program to tell the seasons given the date.

# get input.
month = input().capitalize()
day = int(input())

# check for valid date.
if day > 31:
    print('Invalid')
else:
    # check for seasons else invalid month.
    if month == 'March' and day > 19:
        print('Spring')
    elif month == 'June' and day > 20:
        print('Summer')
    elif month == 'September' and day > 21:
        print('Autumn')
    elif month == 'December' and day > 20:
        print('Winter')
    elif month in ['April', 'May', 'June']:
        print('Spring')
    elif month in ['July', 'August', 'September']:
        print('Summer')
    elif month in ['October', 'November', 'December']:
        print('Autumn')
    elif month in ['January', 'February', 'March']:
        print('Winter')
    else:
        print('Invalid')