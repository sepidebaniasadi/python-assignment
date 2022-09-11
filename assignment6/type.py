from tabulate import tabulate as t
from colorama import Fore,Back,Style
def type(file):
   w=file.split('.')
   ans=w[-1]
   return(ans)
file=input(Fore.BLUE+'enter your name file:'+Style.RESET_ALL)
c=type(file)
print(Back.LIGHTRED_EX+"table of file name and type"+Style.RESET_ALL)
ta=[['file name','file type'],
[file,c]]
print(t(ta,tablefmt='fancy_grid'))
