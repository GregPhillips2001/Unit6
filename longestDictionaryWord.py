#Greg Phillips
#12/6/17
#longestDictionaryWord.py 

dictionary = open('engmix.txt')

word = 0
for words in dictionary:
    if word < len(words):
        word = words
print(word)
