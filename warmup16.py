#Greg Phillips
#12/11/17
#warmup16.py - how to read a file

dictionary = open('engmix.txt')

for w in dictionary:
    if w[0] == 'g':
        if w[-1] == 'p':
            print(w)
