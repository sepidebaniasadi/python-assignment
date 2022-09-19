
import time
from tabulate import tabulate as t
from colorama import Fore,Back,Style
from pyfiglet import Figlet as p
import emoji
import random as ra
f=p(justify='center',font='slant')
start=time.time()

def wlcm():
    print(f.renderText("welcome to"'\n'" Tic Tac Toe game"))
def catg():
    table=[[Fore.BLACK+Back.RED+"1)game with pc"+emoji.emojize("💻")+Style.RESET_ALL],
    [Fore.BLACK+Back.RED+"2)game with your friend"+emoji.emojize("👩👧")+Style.RESET_ALL]]
    print(t(table,tablefmt='fancy_grid'))
    


def board():
        brd2=[[Fore.RED+Back.LIGHTWHITE_EX+' A '+Style.RESET_ALL,Fore.RED+Back.LIGHTYELLOW_EX+' B '+Style.RESET_ALL,Fore.RED+Back.LIGHTWHITE_EX+' C '+Style.RESET_ALL],
        [Fore.RED+Back.YELLOW+' D '+Style.RESET_ALL,Fore.RED+Back.CYAN+' E '+Style.RESET_ALL,Fore.RED+Back.LIGHTMAGENTA_EX+' F '+Style.RESET_ALL],
        [Fore.RED+Back.GREEN+' G '+Style.RESET_ALL,Fore.RED+Back.LIGHTMAGENTA_EX+' H '+Style.RESET_ALL,Fore.RED+Back.BLUE+' I '+Style.RESET_ALL]]
        
        for i in range(3):
            for j in range(3):
                    print(brd2[i][j],end=' ')
            print()

def char(pl1):
    while True:
        if pl1=='1':
            character=emoji.emojize("🟡")
            return(character)
        elif pl1=='2':
            character=emoji.emojize("🟢")
            return(character)
        elif pl1=='3':
            character=emoji.emojize("🟠")
            return(character)
        elif pl1=='4':
            character=emoji.emojize("🟣")
            return(character)
        else:
            print("wrong")
            print(Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+"choice player one : ",emoji.emojize("🤪")+Style.RESET_ALL)
            pl1=input(" ")
            continue
def char2(pl2):
    while True:
        if pl2=='1':
            character=emoji.emojize("🟡")
            return(character)
            break
        elif pl2=='2':
            character=emoji.emojize("🟢")
            return(character)
            break
        elif pl2=='3':
            character=emoji.emojize("🟠")
            return(character)
            break
        elif pl2=='4':
            character=emoji.emojize("🟣")
            return(character)
            break
        else:
            print("wrong")
            print(Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+"choice  player tow: ",emoji.emojize("🤪")+Style.RESET_ALL)
            pl2=input(" ")
            continue

        
def select1():
    
        print(Back.LIGHTMAGENTA_EX+Fore.YELLOW+"What do you like your character to be? "+Style.RESET_ALL,'\n')
        table=[[Fore.BLACK+Back.LIGHTWHITE_EX+"1)"+emoji.emojize("🟡")+Style.RESET_ALL],
        [Fore.BLACK+Back.WHITE+"2)"+emoji.emojize("🟢")+Style.RESET_ALL],
        [Fore.BLACK+Back.WHITE+"3)"+emoji.emojize("🟠")+Style.RESET_ALL],
        [Fore.BLACK+Back.WHITE+"4)"+emoji.emojize("🟣")+Style.RESET_ALL]]
        print(t(table,tablefmt="orgtbl"))
def pos(plch1,pl1):
        while True:
            if plch1.upper()=='A' and list2[0][0]==plch1.upper():
                
                list2[0][0]=char(pl1)
                listeq.append(plch1.upper())
                
                break
            elif plch1.upper()=='B' and list2[0][1]==plch1.upper():
                
                list2[0][1]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='C' and  list2[0][2]==plch1.upper():
                
                list2[0][2]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='D' and list2[1][0]==plch1.upper():
                
                list2[1][0]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='E' and list2[1][1]==plch1.upper():
                
                list2[1][1]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='F' and list2[1][2]==plch1.upper():
                
                list2[1][2]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='G'and list2[2][0]==plch1.upper():
                
                list2[2][0]=char(pl1)
                listeq.append(plch1.upper())
                break
            elif plch1.upper()=='H' and list2[2][1]==plch1.upper():
                
                list2[2][1]=char(pl1)
                listeq.append(plch1.upper())
                
                
                break
            elif plch1.upper()=='I' and list2[2][2]==plch1.upper():
                
                list2[2][2]=char(pl1)
                listeq.append(plch1.upper())
                
                
                break
            else:
                print('wrong')
                plch1=input("pos? ")
                
                
                continue
        listpc1.remove(plch1.upper())
        for i in range(3):
            for j in range(3):
                print(list2[i][j],end=' ')
            print('\n')
       
        

def pos2(plch2,pl2):
        while True:
            if plch2.upper()=='A' and list2[0][0]==plch2.upper():
                
                list2[0][0]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='B' and list2[0][1]==plch2.upper():
                
                list2[0][1]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='C' and  list2[0][2]==plch2.upper():
                
                list2[0][2]=char(pl2)
                break
            elif plch2.upper()=='D' and list2[1][0]==plch2.upper():
                
                list2[1][0]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='E' and list2[1][1]==plch2.upper():
                
                list2[1][1]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='F' and list2[1][2]==plch2.upper():
                
                list2[1][2]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='G'and list2[2][0]==plch2.upper():
                
                list2[2][0]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='H' and list2[2][1]==plch2.upper():
                
                list2[2][1]=char(pl2)
                listeq.append(plch2.upper())
                break
            elif plch2.upper()=='I' and list2[2][2]==plch2.upper():
                
                list2[2][2]=char(pl2)
                listeq.append(plch2.upper())
                break
            else:
                print('wrong')
                plch2=input("pos? ")
                continue
        
        for i in range(3):
            for j in range(3):
                print(list2[i][j],end=' ')
            print('\n')
        
def pospc(pc1):
    pc=emoji.emojize("💻")
    while True:
            if pc1=='A'and list2[0][0]==pc1:
                listeq.append(pc)
                list2[0][0]=pc
                break
            elif pc1=='B'and list2[0][1]==pc1:
                listeq.append(pc)
               
                list2[0][1]=pc
                break
            elif pc1=='C'and list2[0][2]==pc1:
                listeq.append(pc)
                
                list2[0][2]=pc
                break
            elif pc1=='D'and list2[1][0]==pc1:
                listeq.append(pc)
                
                list2[1][0]=pc
                break
            elif pc1=='E'and list2[1][1]==pc1:
                listeq.append(pc)
                list2[1][1]=pc
                break
            elif pc1=='F'and list2[1][2]==pc1:
                listeq.append(pc)
                list2[1][2]=pc
                break
            elif pc1=='G'and list2[2][0]==pc1:
                listeq.append(pc)
                list2[2][0]=pc
                break
            elif pc1=='H'and list2[2][1]==pc1:
                listeq.append(pc)
                list2[2][1]=pc
                break
            elif pc1=='I'and list2[2][2]==pc1:
                listeq.append(pc)
                list2[2][2]=pc
                break
            
    for i in range(3):
        for j in range(3):
            print(list2[i][j],end=' ')
        print('\n')



def  win(pl1):
    pc=emoji.emojize("💻")
    if list2[0][0]==char(pl1) and list2[0][1]==char(pl1) and list2[0][2]==char(pl1) or list2[1][0]==char(pl1) and list2[1][1]==char(pl1) and list2[1][2]==char(pl1) or list2[2][0]==char(pl1) and list2[2][1]==char(pl1) and list2[2][2]==char(pl1) or list2[0][0]==char(pl1) and list2[1][0]==char(pl1) and list2[2][0]==char(pl1) or list2[0][1]==char(pl1) and list2[1][1]==char(pl1) and list2[2][1]==char(pl1) or list2[0][2]==char(pl1) and list2[1][2]==char(pl1) and list2[2][2]==char(pl1) or list2[0][0]==char(pl1) and list2[1][1]==char(pl1) and list2[2][2]==char(pl1) or list2[0][2]==char(pl1) and list2[1][1]==char(pl1) and list2[2][0]==char(pl1):
             c=True
             return(c)
    elif list2[0][0]==pc and list2[0][1]==pc and list2[0][2]==pc or list2[1][0]==pc and list2[1][1]==pc and list2[1][2]==pc or list2[2][0]==pc and list2[2][1]==pc and list2[2][2]==pc or list2[0][0]==pc and list2[1][0]==pc and list2[2][0]==pc or list2[0][1]==pc and list2[1][1]==pc and list2[2][1]==pc or list2[0][2]==pc and list2[1][2]==pc and list2[2][2]==pc or list2[0][0]==pc and list2[1][1]==pc and list2[2][2]==pc or list2[0][2]==pc and list2[1][1]==pc and list2[2][0]==pc:
            c='sad'
            return(c)
    elif len(listeq)==9:
        c='eq'
        return(c)
def  win2(pl1,pl2):
    pc=emoji.emojize("💻")
    if list2[0][0]==char(pl1) and list2[0][1]==char(pl1) and list2[0][2]==char(pl1) or list2[1][0]==char(pl1) and list2[1][1]==char(pl1) and list2[1][2]==char(pl1) or list2[2][0]==char(pl1) and list2[2][1]==char(pl1) and list2[2][2]==char(pl1) or list2[0][0]==char(pl1) and list2[1][0]==char(pl1) and list2[2][0]==char(pl1) or list2[0][1]==char(pl1) and list2[1][1]==char(pl1) and list2[2][1]==char(pl1) or list2[0][2]==char(pl1) and list2[1][2]==char(pl1) and list2[2][2]==char(pl1) or list2[0][0]==char(pl1) and list2[1][1]==char(pl1) and list2[2][2]==char(pl1) or list2[0][2]==char(pl1) and list2[1][1]==char(pl1) and list2[2][0]==char(pl1):
             c=True
             return(c)
    elif list2[0][0]==pc and list2[0][1]==pc and list2[0][2]==pc or list2[1][0]==pc and list2[1][1]==pc and list2[1][2]==pc or list2[2][0]==pc and list2[2][1]==pc and list2[2][2]==pc or list2[0][0]==pc and list2[1][0]==pc and list2[2][0]==pc or list2[0][1]==pc and list2[1][1]==pc and list2[2][1]==pc or list2[0][2]==pc and list2[1][2]==pc and list2[2][2]==pc or list2[0][0]==pc and list2[1][1]==pc and list2[2][2]==pc or list2[0][2]==pc and list2[1][1]==pc and list2[2][0]==pc:
            c='sad'
            return(c)
    elif list2[0][0]==char2(pl2) and list2[0][1]==char2(pl2) and list2[0][2]==char2(pl2) or list2[1][0]==char2(pl2) and list2[1][1]==char2(pl2) and list2[1][2]==char2(pl2) or list2[2][0]==char2(pl2) and list2[2][1]==char2(pl2) and list2[2][2]==char2(pl2) or list2[0][0]==char2(pl2) and list2[1][0]==char2(pl2) and list2[2][0]==char2(pl2) or list2[0][1]==char2(pl2) and list2[1][1]==char2(pl2) and list2[2][1]==char2(pl2) or list2[0][2]==char2(pl2) and list2[1][2]==char2(pl2) and list2[2][2]==char2(pl2) or list2[0][0]==char2(pl2) and list2[1][1]==char2(pl2) and list2[2][2]==char2(pl2) or list2[0][2]==char2(pl2) and list2[1][1]==char2(pl2) and list2[2][0]==char2(pl2):
             c='t2'
             return(c)
    elif len(listeq)==9:
        c='equ'
        return(c)
   
       
    

    
        
                

        
def run(select,listpc1):
    if select=='1':
            print(Fore.RED,Back.LIGHTWHITE_EX+"what's your name "+emoji.emojize("😍")+Style.RESET_ALL)
            name=input(" ")
            select1()
            
            print(Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+"choice : "+emoji.emojize("🤪")+Style.RESET_ALL)
            pl1=input(" ")
            print("\n")

            table=[[Back.LIGHTMAGENTA_EX+name+Style.RESET_ALL,char(pl1)],
            [Back.LIGHTMAGENTA_EX+'pc  '+Style.RESET_ALL,emoji.emojize("💻")]]
            print((t(table,tablefmt="fancy_grid")))
            board()
            while True:
                        plch1=input('pos? ')
                        
                        pos(plch1,pl1)
                        
                        print('='*10)
                        
                        
                        if len(listeq)<9:
                            
                            pc1=ra.choice(listpc1)
                            
                            listpc1.remove(pc1)
                            
                            pospc(pc1)
                            
                        if  win(pl1)==True:
                            print(Back.LIGHTMAGENTA_EX+'hoooray',name,'winner',emoji.emojize("😁")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
                            
                        elif  win(pl1)=='sad':
                            print(Back.LIGHTMAGENTA_EX+'oh',name,'you are faild',emoji.emojize("😭")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
                        elif win(pl1)=='eq':
                            print(Back.LIGHTMAGENTA_EX+'oh nobody winner',emoji.emojize("😭")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
    elif select=='2':            

            print(Fore.RED,Back.LIGHTWHITE_EX+"what's your name player one:"+emoji.emojize("😍")+Style.RESET_ALL)
            name=input(" ")
            print(Fore.RED,Back.LIGHTWHITE_EX+"what's your name player tow::"+emoji.emojize("😍")+Style.RESET_ALL)
            name2=input(" ")
            select1()
            
            print(Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+"choice : ",name,emoji.emojize("🤪")+Style.RESET_ALL)
            pl1=input(" ")
            print("")
            print(Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+"choice : ",name2,emoji.emojize("🤪")+Style.RESET_ALL)
            pl2=input(" ")
            print("\n")

            table=[[Back.LIGHTMAGENTA_EX+name+Style.RESET_ALL,char(pl1)],
            [Back.LIGHTMAGENTA_EX+name2+Style.RESET_ALL,char2(pl2)]]
            print((t(table,tablefmt="fancy_grid")))
            board()
            while True:
                        plch1=input('pos? ')
                        
                        pos(plch1,pl1)
                        if win2(pl1,pl2)== True:
                            print(Back.LIGHTMAGENTA_EX+'hoooray',name,'winner',emoji.emojize("😁")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
                            
                        elif win2(pl1,pl2)=='sad':
                            print(Back.LIGHTMAGENTA_EX+'oh',name,'you are faild',emoji.emojize("😭")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break  
                        plch2=input('pos? ')
                        pos2(plch2,pl2)
                        print('='*10)
                        
                        if win2(pl1,pl2)== True:
                            print(Back.LIGHTMAGENTA_EX+'hoooray',name,'winner',emoji.emojize("😁")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
                            
                        elif win2(pl1,pl2)=='sad':
                            print(Back.LIGHTMAGENTA_EX+'oh',name,'you are faild',emoji.emojize("😭")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break  
                        elif win2(pl1,pl2)=='t2':
                            print(Back.LIGHTMAGENTA_EX+'hoooray',name2,'winner',emoji.emojize("😁")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break
                        elif win2(pl1,pl2)=='equ':
                            print(Back.LIGHTMAGENTA_EX+'oh nobody winner',emoji.emojize("😭")+Style.RESET_ALL)
                            res=time.time()-start
                            print(Back.LIGHTRED_EX+'time= ',res,emoji.emojize("🕐")+Style.RESET_ALL)
                            break  

listpc1=['A','B','C','D','E','F','G','H','I']
list2=[['A','B','C'],['D','E','F'],['G','H','I' ]]
listeq=[]
wlcm()
catg()
print(Fore.LIGHTMAGENTA_EX,Back.LIGHTWHITE_EX+" choice: "+emoji.emojize("🤪")+Style.RESET_ALL)
select=input(" ")

run(select,listpc1)

