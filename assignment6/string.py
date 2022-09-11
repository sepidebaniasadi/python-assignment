from colorama import Fore,Back,Style
def string(string):
    element=["." , "," , "/" , "\\" , "[" , "]" , "{" , "}" , "!" , "#" , "&" , "(" , 
                 ")" , "*" , "^" , ":" , ";" , "\'" , "\"" , "<" , ">" , "|" , "$" , "%" ,
                 "~" , "`" , "@" , "?" ]
    for elments in element:
     string= string.replace(elments , " ")

     word = string.split()
     cw = len(word)

    return(cw)


stri=input(Back.LIGHTMAGENTA_EX+"enter your string^_^ : "+Style.RESET_ALL)
b=string(stri)
print(Fore.CYAN+"you'r string have "+Style.RESET_ALL+Fore.CYAN+str(b)+Style.RESET_ALL+Fore.CYAN+" words")
