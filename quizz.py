#Greg Phillips
#12/13/17
#quizz.py 

dictionary = open('engmix.txt')

wordcount = 0
for w in dictionary:
    if w.strip() != '':
        if w.strip()[0] == 'r':
            wordcount += 1
print('There are', wordCount, 'words in the dictionary that start with r.')