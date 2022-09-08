from audioop import reverse
from tabulate import tabulate as t


word=input("word: ")
list=[]
list2=[]
if len(word)%2==0:
    half_word=int(len(word)/2)
    slice1=word[:half_word]
    for letter in slice1:
        list.append(letter)
        continue
    list.reverse()
    slice2=word[half_word:]
    for letters in slice2:
        list2.append(letters)
        continue
    if list==list2:
        print("you'r word is palindrome")
        table=[['word',word],
        ['palindrome',word]]
        print(t(table,tablefmt='fancy_grid'))
    else:
        list2.reverse()
        b=list2+list
        c="".join(b)
        print("you'r word isn't palindrome")
        table=[['word',word],
        ['palindrome',c]]
        print(t(table,tablefmt='fancy_grid'))
else:
    half_word=int(len(word)/2)
    slice1=word[:half_word]
    for letter in slice1:
        list.append(letter)
        continue
    list.reverse()
    slice2=word[half_word+1:]
    for letters in slice2:
        list2.append(letters)
        continue
    if list==list2:
        print("you'r word is palindrome")
        table=[['word',word],
        ['palindrome',word]]
        print(t(table,tablefmt='fancy_grid'))
    else:
        list2.reverse()
        b=list2+list
        c="".join(b)
        print("you'r word isn't palindrome")
        table=[['word',word],
        ['palindrome',c]]
        print(t(table,tablefmt='fancy_grid'))


        

        
   