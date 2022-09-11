from cmath import sqrt
from tabulate import tabulate as t
from colorama import Back,Fore,Style


import math as m
def darajehdo(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta>0:
        x1=(-b+m.sqrt(delta))/2*a
        x2=(-b-m.sqrt(delta))/2*a
        return(Fore.RED+"you have 2 answer:"+Style.RESET_ALL+Fore.BLUE+str(x1)+Style.RESET_ALL+Fore.RED+' and '+str(x2)+Style.RESET_ALL)
    elif delta<0:
        return(Fore.LIGHTRED_EX+"no answer ..."+Style.RESET_ALL)
    elif delta==0:
        x2=(-b-m.sqrt(delta))/2*a
        return(Fore.RED+"you have 1 answer:"+Style.RESET_ALL+Fore.BLUE+str(x2)+Style.RESET_ALL)
    else:
        return("wrong")

        

a=float(input('enter a: '))
b=float(input("enter b: "))
c=float(input("enter c: "))
ans=darajehdo(a,b,c)
print(Fore.CYAN+Back.LIGHTMAGENTA_EX+"table answers"+Style.RESET_ALL)
table=[['a',a],
['b',b],
['c',c],
['answer',ans]]
print(t(table,tablefmt='fancy_grid'))

