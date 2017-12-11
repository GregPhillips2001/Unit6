#Greg Phillips
#12/11/17
#warmup16.py - how to read a file

dictionary = open('engmix.txt')

for w in dictionary:
    if w.strip() != '':
        if w.strip()[0] == 'g'and w.strip()[-1] == 'p':
            print(w)
