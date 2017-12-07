#Greg Phillips
#12/7/17
#howManyWords.py

dictionary = open('engmix.txt')

#finding number of words
words = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in dictionary:
    for i in range(
    if len(word) == 1:
        wordCount += 1
        
print('There are', wordCount, 'two letter words in the dictionary.')


