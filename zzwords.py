#Greg Phillips
#12/7/17
#zzword.py

dictionary = open('engmix.txt')

for word in dictionary:
    if 'zz' in word: 
        print(word.strip()) #stops it from going to the next line when printed
