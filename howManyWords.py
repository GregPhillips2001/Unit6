#Greg Phillips
#12/7/17
#howManyWords.py

dictionary = open('engmix.txt')

#finding number of words
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for w in dictionary:
    length = len(w)
    for i in range(1,30):
        if length == i: 
            words[i-1] += 1
            
for i in range(1,25):
    print('There are', words[i], i, 'letter words in the dictionary.')


