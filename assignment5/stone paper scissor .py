import random as ra
from tabulate import tabulate as ta 
from colorama import Fore,Back,Style

count1=0
count2=0
a='stone'
b='paper'
c='scissor'
list=['stone','paper','scissor']
table=[["You prefer to play single player or doubles?"],
["1)single"],
["2)doubles"]]
print(ta(table,tablefmt='fancy_grid'))
select=int(input(Fore.BLUE+'choice : '+Style.RESET_ALL))
if select==2:
        name=input("please enter your name: ")
        name2=input("please enter your name: ")
        
        table2=[["well,You'd like the game to be multi-point..."],
        ["1)1 point"],
        ["2)3 point"],
        ["3)5 point"]]
    
        print(ta(table2,tablefmt='fancy_grid'))
        select2=int(input(Fore.BLUE+'choice : '+Style.RESET_ALL))
        if select2==1:
            #double 1point
            while True:
                    
                table1=[["select:"],
                    ['a)stone'],
                    ['b)paper'],
                    ['c)scissor']]
                print(ta(table1,tablefmt='fancy_grid'))
                select3=input(Fore.BLUE+'choice : '+Style.RESET_ALL)
                select4=input(Fore.BLUE+'choice : '+Style.RESET_ALL)
                if(select3=='a' and select4=='c') or (select3=='b' and select4=='a') or (select3=='c' and select4=='b'):
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    table=[[name,select3],
                                ['name',select4]]
                    print(ta(table,tablefmt='fancy_grid'))
                    break
                elif(select3=='a' and select4=='c') or (select3=='b' and select4=='b' )or( select3=='b' and select4=='b' ):
                    print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                    continue
                elif(select3=='c' and select4=='a') or( select3=='a' and select4=='b' )or (select3=='b' and select4=='c'):
                    print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                    table=[[name,select3],
                                ['name',select4]]
                    print(ta(table,tablefmt='fancy_grid'))
                    break
                else:
                    print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)
        elif select2==2:
            
            #double 3point
            
            while True:
                if count1<3 and count2<3:
                    
                        table1=[["select:"],
                        ['a)stone'],
                        ['b)paper'],
                        ['c)scissor']]
                        print(ta(table1,tablefmt='fancy_grid'))
                        select3=input('\033[33;1m'+'choice : ')
                        select4=input('\033[33;1m'+'choice : ')
                        if(select3=='a' and select4=='c') or (select3=='b' and select4=='a') or (select3=='c' and select4=='b'):
                            table=[[name,select3],
                                ['name',select4]]
                            print(ta(table,tablefmt='fancy_grid'))
                            print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                            count1+=1
                            print( name,':',select3,'\n'+name2,':',select4,'\n')
                        elif(select3=='a' and select4=='c') or (select3=='b' and select4=='b') or (select3=='b' and select4=='b' ):
                            print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                            continue
                        elif(select3=='c' and select4=='a') or (select3=='a' and select4=='b') or (select3=='b' and select4=='c'):
                            table=[[name,select3],
                                [name2,select4]]
                            print(ta(table,tablefmt='fancy_grid'))
                            print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                            count2+=1
                            
                        else:
                            
                            print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)
                else:
                        table=[['name','point'],
                        [name,count1],
                        [name2,count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break

        elif select2==3:
            
            #double 5point
            
            while True:
                if count1<5 and count2<5:
                    
                        table1=[["select:"],
                        ['a)stone'],
                        ['b)paper'],
                        ['c)scissor']]
                        print(ta(table1,tablefmt='fancy_grid'))
                        select3=input('\033[33;1m'+'choice : ')
                        select4=input('\033[33;1m'+'choice : ')
                        if(select3=='a' and select4=='c') or (select3=='b' and select4=='a') or (select3=='c' and select4=='b'):
                            table=[[name,select3],
                                ['name',select4]]
                            print(ta(table,tablefmt='fancy_grid'))
                            print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                            count1+=1
                            print( name,':',select3,'\n'+name2,':',select4,'\n')
                        elif(select3=='a' and select4=='c') or (select3=='b' and select4=='b') or (select3=='b' and select4=='b' ):
                            print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                            continue
                        elif(select3=='c' and select4=='a') or (select3=='a' and select4=='b') or (select3=='b' and select4=='c'):
                            table=[[name,select3],
                                [name2,select4]]
                            print(ta(table,tablefmt='fancy_grid'))
                            print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name2+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                            count2+=1
                            
                        else:
                            
                            print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL)

                else:
                        table=[['name','point'],
                        [name,count1],
                        [name2,count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break
          
elif select==1:
        name=input("please enter your name: ")
        table2=[["well,You'd like the game to be multi-point..."],
        ["1)1 point"],
        ["2)3 point"],
        ["3)5 point"]]
        print(ta(table2,tablefmt='fancy_grid'))
        select2=int(input(Fore.BLUE+'choice : '+Style.RESET_ALL))
        if select2==1:
            while True:
                        table1=[["select:"],
                        ['a)stone'],
                        ['b)paper'],
                        ['c)scissor']]
                        print(ta(table1,tablefmt='fancy_grid'))
                        select3=input(Fore.BLUE+'choice : '+Style.RESET_ALL)

                        if (select3=="a" and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='stone')or (select3=='c' and ra.choice(list)=='paper'):
                         
                                table=[[name,select3],
                                ['pc',ra.choice(list)]]
                                print(ta(table,tablefmt='fancy_grid'))
                                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                               
                                break
                        elif (select3=='c' and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='paper') or (select3=='a' and ra.choice(list)=='stone'):
                            print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                            continue
                        elif  (select3=="a" and ra.choice(list)=='paper') or (select3=='b' and ra.choice(list)=='scissor')or (select3=='c' and ra.choice(list)=='stone'):
                            table=[[name,select3],
                                ['pc',ra.choice(list)]]
                            print(ta(table,tablefmt='fancy_grid'))
                            print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                            break
                        else:
                            print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)
        #single3point 
        elif select2==2:
            while True:
                if count1<3 and count2<3:
                            table1=[["select:"],
                            ['a)stone'],
                            ['b)paper'],
                            ['c)scissor']]
                            print(ta(table1,tablefmt='fancy_grid'))
                            select3=input(Fore.BLUE+'choice : '+Style.RESET_ALL)

                            if (select3=="a" and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='stone')or (select3=='c' and ra.choice(list)=='paper'):
                                count1+=1
                                table=[[name,select3],
                                ['pc',ra.choice(list)]]
                                print(ta(table,tablefmt='fancy_grid'))
                                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                                
                            elif (select3=='c' and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='paper') or (select3=='a' and ra.choice(list)=='stone'):
                                print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                                continue
                            elif  (select3=="a" and ra.choice(list)=='paper') or (select3=='b' and ra.choice(list)=='scissor')or (select3=='c' and ra.choice(list)=='stone'):
                        
                                count2+=1
                                table=[[name,select3],
                                ['pc',ra.choice(list)]]
                                print(ta(table,tablefmt='fancy_grid'))
                                print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                            else:
                                print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)

                else:
                        table=[['name','point'],
                        [name,count1],
                        ['PC',count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break
    #single5point 
        elif select2==3:
            while True:
                if count1<5 and count2<5:
                            table1=[["select:"],
                            ['a)stone'],
                            ['b)paper'],
                            ['c)scissor']]
                            print(ta(table1,tablefmt='fancy_grid'))
                            select3=input(Fore.BLUE+'choice : '+Style.RESET_ALL)

                            if (select3=="a" and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='stone')or (select3=='c' and ra.choice(list)=='paper'):
                                
                                count1+=1
                                table=[[name,select3],
                                ['pc',ra.choice(list)]]
                                print(ta(table,tablefmt='fancy_grid'))
                                print(Fore.GREEN+'hooray,'+Back.LIGHTCYAN_EX+name+Style.RESET_ALL+Fore.GREEN+' is winer'+Style.RESET_ALL)
                            elif (select3=='c' and ra.choice(list)=='scissor') or (select3=='b' and ra.choice(list)=='paper') or (select3=='a' and ra.choice(list)=='stone'):
                                print(Fore.LIGHTYELLOW_EX+"equal"+Style.RESET_ALL)
                                continue
                            elif  (select3=="a" and ra.choice(list)=='paper') or (select3=='b' and ra.choice(list)=='scissor')or (select3=='c' and ra.choice(list)=='stone'):
                                
                                count2+=1
                                table=[[name,select3],
                                ['pc',ra.choice(list)]]
                                print(ta(table,tablefmt='fancy_grid'))
                                print(Fore.RED+'oh, you are faild :('+Style.RESET_ALL)
                            else:
                                print(Fore.LIGHTRED_EX+'wrong'+Style.RESET_ALL+Style.RESET_ALL)
                else:
                        table=[['name','point'],
                        [name,count1],
                        ['PC',count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break
