#Greg Phillips
#12/6/17
#longestDictionaryWord.py 

dictionary = open('engmix.txt')

l = 0
word = ""
for w in dictionary:
    length = len(w)
    if length > l:
        l = length
        word = w
print("The longest word is", word)
print(word, 'has', len(word), 'letters')

