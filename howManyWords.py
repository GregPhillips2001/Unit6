#Greg Phillips
#12/7/17
#howManyWords.py

dictionary = open('engmix.txt')

#finding number of words
wordCount = 0 

for word in dictionary:
    if len(word) == 2:
        wordCount += 1
        
print('There are', wordCount, 'two letter words in the dictionary.')


