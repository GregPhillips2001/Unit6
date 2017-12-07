#Greg Phillips
#12/7/17
#howManyWords.py

dictionary = open('engmix.txt')

#finding number of words
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in dictionary:
    for i in range(1,100):
        if len(word) == i:
            words[i-1] += 1
        
print('There are', wordCount, 'two letter words in the dictionary.')


