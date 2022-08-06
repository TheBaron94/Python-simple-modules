# LAB 7.8
# Adam Schmidt
# A program to import word lists from csv adn count frequencies.

import csv

# Get file and read out each word into a list
file_name = input()
word_list = []
with open(file_name, 'r') as file:
    word_file = csv.reader(file)
    for row in word_file:
        for word in row:
            word_list.append(word)

# Line 15 code adapted from w3Schools.com
# Source: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# retrieved April 2021
# Create a copy of the list with duplicates removed.
word_list_nodup = list(dict.fromkeys(word_list))

# Count and return
for word in word_list_nodup:
    word_count = word_list.count(word)
    print(word, word_count)



