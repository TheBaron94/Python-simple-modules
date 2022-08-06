# LAB 7.9
# Adam schmidt
# a program to sort tv shows and store them in a dict based on seasons

file_name = input()
season_dict = {}
with open(file_name) as file:
    lines = file.readlines()
    count = lines[0].strip
    show = lines[1].strip
    season_dict.update({count:show})
    print(season_dict)

