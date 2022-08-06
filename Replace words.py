# LAB 6.19
# Adam Schmidt
# A program to find a replace words in a sentence

# Get input and set variable.
repl_words = input()
list_repl = repl_words.split('  ')
repl_dict = {}

# Make dict with replace words.
for i in list_repl:
    i_split = i.split()
    repl_dict[i_split[0]] = i_split[1]

# Get sentence.
sentence = input()
sentence_split = sentence.split()
sentence_revised = ''

# Iterate through sentence and replace key words
word_count = 0
for word in sentence_split:
    if word_count > 0:
        sentence_revised += ' '
    if word in repl_dict.keys():
        sentence_revised += repl_dict.get(word)
        word_count +=1
    else:
        sentence_revised += word
        word_count +=1


print(sentence_revised)


