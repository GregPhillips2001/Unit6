#Greg Phillips
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

#finding number of words
wordCount = 0 
for word in dictionary:
    if 'greg' in word:
        print(word)
    wordCount += 1
print('There are', wordCount, 'words in the dictionary.')
