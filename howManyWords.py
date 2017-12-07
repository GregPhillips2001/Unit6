#Greg Phillips
#12/7/17
#howManyWords.py

dictionary = open('engmix.txt')

#finding number of words
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for w in dictionary:
    length = len(w)
    if length == 2: 
        words[0] += 1
            

print('There are', words[0], 'one letter words in the dictionary.')


