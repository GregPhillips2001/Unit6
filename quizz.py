#Greg Phillips
#12/13/17
#quizz.py 

#program 2
"""dictionary = open('engmix.txt')

wordcount = 0
for w in dictionary:
    if w.strip() != '':
        if w.strip()[0] == 'r':
            wordcount += 1
print('There are', wordcount, 'words in the dictionary that start with r.')"""

#program 3
"""dictionary = open('engmix.txt')
number = int(input('enter a number; '))

for w in dictionary:
    if len(w) == number+1: 
        print(w)
        break"""
        
#program 3
dictionary = open('engmix.txt')

wordcount = 0
letter = input('enter a letter; ')
for w in dictionary:
    if w.strip() != '':
        if letter not in w:
            wordcount += 1
print('There are', wordcount, 'words in the dictionary do not have the letter', letter)
            
            
