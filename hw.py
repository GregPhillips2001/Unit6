#Greg Phillips
#12/7/17
#hw.py 

#is word in dictionary
dictionary = open('engmix.txt')

word = input('enter a word, ')

yes = False
for w in dictionary:
    if w.strip()==word: 
        yes = True
        break

if yes == True:
    print(word, 'is in the dictionary')
else:
    print(word, 'is not in the dictionary')

#dictionary list
dictionary = open('engmix.txt')
list = []

for w in dictionary:
    list.append[w.strip()]
num = input('enter a number, ')
print('enter a number, ')