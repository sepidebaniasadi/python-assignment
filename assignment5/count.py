import math
from tabulate import tabulate as t
n=int(input("How many sentences do you want to check?"))
I=1
for i in range(n):
    cchar=0
    cword=0
    ccom=-1
    ccom1=-1
    clower=0
    cupper=0
    cnum=0
    cc=-1
    sentence=input("sentens:")
    for char in sentence:
        cchar+=1
        ccomi=-1
    for comma in sentence.split("."):
        ccom+=1
    for comma2 in sentence.split(","):
        ccom1+=1
    for space in sentence.split():
        cc+=1
    for word in sentence.split():
        if word=='.' or word==',':
            ccomi+=1
    for num in sentence:
        if num=='1' or num=='2'or num=='3' or num=='4' or num=='5' or num=='6' or num=='7' or num=='8' or num=='9' or num=='0':
            cnum+=1
        
    for letter in sentence:
        if letter=='a' or letter=='b'or letter=='c'or letter=='d'or letter=='e'or letter=='f'or letter=='g'or letter=='h'or letter=='i'or letter=='j'or letter=='k'or  letter=='l'or letter=='m'or letter=='n'or letter=='o'or letter=='p'or letter=='q'or letter=='r'or letter=='s'or letter=='t'or letter=='u'or letter=='v'or letter=='w'or letter=='x'or letter=='y'or letter=='z':
            clower+=1
            continue
        
        elif letter=='A' or letter=='B'or letter=='C'or letter=='D'or letter=='E'or letter=='F'or letter=='G'or letter=='H'or letter=='I'or letter=='J'or letter=='K'or letter=='L'or letter=='M'or letter=='N'or letter=='O'or letter=='P'or letter=='Q'or letter=='R'or letter=='S'or letter=='T'or letter=='U'or letter=='V'or letter=='W'or letter=='X'or letter=='Y'or letter=='Z':
            cupper+=1
            continue
    letter=cupper+clower
    
    table=[['comma',ccom+ccom1],
        ['character',cchar],
        ['word',cc-ccomi],
        ['space',cc],
        ['letter',letter],
        ['caps letter',cupper],
        ['small letter',clower],
        ['number',cnum]]
    print(t(table,tablefmt='fancy_grid'))



        
