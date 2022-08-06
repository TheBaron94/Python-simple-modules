# LAB 4.14
# Adam Schmidt
# Given a line of text, output the number of characters
# excluding spaces, periods, or commas.

user_input = input()
count = 0

# count out the letters using a for loop.
for i in user_input:
    if i == ' ':
        continue
    if i == ',':
        continue
    if i == '.':
        continue
    count += 1

# Print final count.
print(count)
