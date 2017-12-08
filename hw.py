#Greg Phillips
#12/7/17
#hw.py 

#
dictionary = open('engmix.txt')

word = input('enter a word, ')

for w in dictionary:
    yes = false
    if word == w: 
        yes = true
if yes == true:
    print(word, 'is not in the dictionary')
else:
    print(word, 'is in the dictionary')
