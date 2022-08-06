# LAB 6.18
# Adam Schmidt
# a program to count word frequencies in a given string.

# get input from user and split into list
given_words = input()
list_words = given_words.split()

# count each word and return word and value.
for word in list_words:
    word_count = list_words.count(word)
    print(word, word_count)