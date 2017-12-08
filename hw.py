#Greg Phillips
#12/7/17
#hw.py 

dictionary = open('engmix.txt')

word = input('enter a word, ')

for w in dictionary:
    if word in w: 
        break
print(word, 'is in the dictionary')
