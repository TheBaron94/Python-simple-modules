# LAB 4.16
# Adam Schmidt
# A program to take a given character and print a triangle to the given height

triangle_char = input('Enter a character:\n')
triangle_char = triangle_char + ' '
triangle_height = int(input('Enter triangle height:\n'))
height = 0

while triangle_height >= 0:
    print(triangle_char*height)
    triangle_height -= 1
    height += 1
