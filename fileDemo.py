#Greg Phillips
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

#finding number of words
wordCount = 0 
for word in dictionary:
    if 'greg' in word: #looks for words with greg in it
        print(word.strip()) #stops it from going to the next line when printed
    wordCount += 1
print('There are', wordCount, 'words in the dictionary.')
