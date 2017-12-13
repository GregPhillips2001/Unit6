#Greg Phillips
#12/13/17
#quizz.py 

dictionary = open('engmix.txt')

for w in dictionary:
    if w.strip() != '':
        if w.strip()[0] == 'r':
            print(w)
        