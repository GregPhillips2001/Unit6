#Greg Phillips
#12/6/17
#longestDictionaryWord.py 

dictionary = open('engmix.txt')

word = 1
for words in dictionary:
    if word < words:
        word = words
print(word)
