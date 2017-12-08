#Greg Phillips
#12/7/17
#hw.py 

#
dictionary = open('engmix.txt')

word = input('enter a word, ')

yes = False
for w in dictionary:
    if word == w: 
        yes = True
        break
if yes == True:
    print(word, 'is not in the dictionary')
else:
    print(word, 'is in the dictionary')
