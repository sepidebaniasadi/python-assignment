from distutils.fancy_getopt import FancyGetopt, fancy_getopt
from tabulate import tabulate
n=int(input('enter your round: '))
list=[]
listt=[]
for i in range(n):
    name=input("enter name:")
    list.append(name)
for name in list:
    if name not in listt:
        listt.append(name)
    else:
        continue
for name in listt:
    n=list.count(name)
    data_table=[['name','counte'],
                [name,(n)]]
    print(tabulate(data_table,headers='firstrow',tablefmt='fancy_grid'))



            


    
            








    

