# LAB 4.15
# Adam Schmidt
# A program to replace letters in given passwords to help strengthen them.

word = input()
passw = ''

# Check and replace letters in given word
for letter in word:
    if letter == 'i':
        passw = passw + '!'
    elif letter == 'a':
        passw = passw + '@'
    elif letter == 'm':
        passw = passw + 'M'
    elif letter == 'B':
        passw = passw + '8'
    elif letter == 'o':
        passw = passw + '.'
    else:
        passw = passw + letter

# Print final password
passw = passw + 'q*s'
print(passw)
