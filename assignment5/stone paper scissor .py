import random as ra
from tabulate import tabulate as ta 
count1=0
count2=0
a='stone'
b='paper'
c='scissor'
list=['r','p','s']
table=[["You prefer to play single player or doubles?"],
["1)single"],
["2)doubles"]]
print(ta(table,tablefmt='fancy_grid'))
select=int(input('\033[33;2m'+'choice : '+'\033[35;2m'))
if select==2:
        name=input("please enter your name: ")
        name2=input("please enter your name: ")
        
        table2=[["well,You'd like the game to be multi-point..."],
        ["1)1 point"],
        ["2)3 point"],
        ["3)5 point"]]
    
        print(ta(table2,tablefmt='fancy_grid'))
        select2=int(input('\033[33;1m'+'choice: '+'\033[30;1m'))
        if select2==1:
            #double 1point
            while True:
                    
                    table1=[["select:"],
                    ['a)stone'],
                    ['b)paper'],
                    ['c)scissor']]
                    print(ta(table1,tablefmt='fancy_grid'))
                    select3=input('\033[33;1m'+'choice : ')
                    select4=input('\033[33;1m'+'choice : ')
                    
                    if select3=='a' and select4=='c':
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            break
                    elif select3=='b' and select4=='a':
                            print(name,":",b,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            break
                    elif select3=='c' and select4=='b':
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            break
                    
                    elif(select3=='a' and select4=='a'):
                                print(name,":",a,'\n'+name2,":",a)
                                print('\033[30,1m'+"equal")
                                continue
                    elif(select3=='b' and select4=='b'):
                                print(name,":",b,'\n'+name2,":",b)
                                print('\033[30,1m'+"equal")
                                continue
                    elif(select3=='c' and select4=='c'):
                                print(name,":",c,'\n'+name2,":",c)
                                print('\033[30,1m'+"equal")
                                continue
                    
                    elif select3=='c' and select4=='a':
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            break
                    elif select3=='b' and select4=='c':
                            print(name,":",a,'\n'+name2,':',b)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            break
                    elif select3=='a' and select4=="b":
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            break
                    else:
                        print('wrong')
                        break
        if select2==2:
            
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
                    
                        if select3=="a" and select4=="c":
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        elif select3=="b" and select4=="a":
                            print(name,":","b",'\n'+name2,':',"a")
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        elif select3=="c" and select4=="b":
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        
                        elif(select3=="a" and select4=="a"):
                                print(name,":",a,'\n'+name2,":",a)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=="b" and select4=="b"):
                                print(name,":",b,'\n'+name2,":",b)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=="c" and select4=="c"):
                                print(name,":",c,'\n'+name2,":",c)
                                print('\033[30,1m'+"equal")
                                continue

                   
                        elif select3=="c" and select4=="a":
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            count2+=1
                            continue
                        elif select3=="a" and select4=="b":
                            print(name,":",a,'\n'+name2,':',b)
                            count2+=1
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            continue
                        elif select3=="b" and select4=="c":
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            count2+=1
                            continue
                else:
                        table=[['name','point'],
                        [name,count1],
                        [name2,count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break
        if select2==3:
            
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
                    
                        if select3=="a" and select4=="c":
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        elif select3=="b" and select4=="a":
                            print(name,":","b",'\n'+name2,':',"a")
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        elif select3=="c" and select4=="b":
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name,'is winer')
                            count1+=1
                            continue
                        
                        elif(select3=="a" and select4=="a"):
                                print(name,":",a,'\n'+name2,":",a)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=="b" and select4=="b"):
                                print(name,":",b,'\n'+name2,":",b)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=="c" and select4=="c"):
                                print(name,":",c,'\n'+name2,":",c)
                                print('\033[30,1m'+"equal")
                                continue

                   
                        elif select3=="c" and select4=="a":
                            print(name,":",c,'\n'+name2,':',a)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            count2+=1
                            continue
                        elif select3=="a" and select4=="b":
                            print(name,":",a,'\n'+name2,':',b)
                            count2+=1
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            continue
                        elif select3=="b" and select4=="c":
                            print(name,":",a,'\n'+name2,':',c)
                            print('\033[32;1m'+'hooray,',name2,'is winer')
                            count2+=1
                            continue
                else:
                        table=[['name','point'],
                        [name,count1],
                        [name2,count2]]
                        print(ta(table,tablefmt='fancy_grid'))
                        break
#single  
elif select==1:
        name=input("please enter your name: ")
        table2=[["well,You'd like the game to be multi-point..."],
        ["1)1 point"],
        ["2)3 point"],
        ["3)5 point"]]
        print(ta(table2,tablefmt='fancy_grid'))
        select2=int(input('\033[33;1m'+'choice: '+'\033[30;1m'))

        #single 1point

        if select2==1:
            while True:
                        table1=[["select:"],
                        ['a)stone'],
                        ['b)paper'],
                        ['c)scissor']]
                        print(ta(table1,tablefmt='fancy_grid'))
                        select3=input('\033[33;1m'+'choice : ')
                        #select3 winner
                        if (select3=="a" and ra.choice(list)=='s'):
                                print(name,":",a,'\n'+'pc:',c)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                break
                        elif (select3=='b' and ra.choice(list)=='r'):
                                print(name,":",b,'\n'+'pc:',a)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                break
                        elif(select3=='c' and ra.choice(list)=='p'):
                                print(name,":",c,'\n'+'pc:',b)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                break

                        
                        elif(select3=='a' and ra.choice(list)=='r'):
                                print(name,":",a,'\n''pc:',a)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=='b' and ra.choice(list)=='p'):
                                print(name,":",b,'\n''pc:',b)
                                print('\033[30,1m'+"equal")
                                continue
                        elif(select3=='c' and ra.choice(list)=='s'):
                                print(name,":",c,'\n''pc:',c)
                                print('\033[30,1m'+"equal")
                                continue

                        elif(select3=='c' and ra.choice(list)=='r') :
                                print(name,":",c,'\n'+'pc:',a)
                                print('\033[32;1m'+'hooray,pc is winer')
                                break
                        elif(select3=='a' and ra.choice(list)=='p'):
                                print(name,":",a,'\n'+'pc:',b)
                                print('\033[32;1m'+'hooray,pc is winer')
                                break
                        elif(select3=='b' and ra.choice(list)=='s'):
                                print(name,":",b,'\n'+'pc:',c)
                                print('\033[32;1m'+'hooray,pc is winer')
                                break
         #single3point 
        elif select2==2:
            while True:
                if count1<3 and count2<3:
                            table1=[["select:"],
                            ['a)stone'],
                            ['b)paper'],
                            ['c)scissor']]
                            print(ta(table1,tablefmt='fancy_grid'))
                            select3=input('\033[33;1m'+'choice : ')
                            
                            if (select3=='a' and ra.choice(list)=='s'):
                                print(name,":",a,'\n'+'pc:',c)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                            elif (select3=='b' and ra.choice(list)=='r'):
                                print(name,":",b,'\n'+'pc:',a)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                            elif(select3=='c' and ra.choice(list)=='p'):
                                print(name,":",c,'\n'+'pc:',b)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                        
                        
                            elif(select3=="a" and ra.choice(list)=='r'):
                                print(name,":",a,'\n''pc:',a)
                                print('\033[30,1m'+"equal")
                                continue
                            elif(select3=="b" and ra.choice(list)=='p'):
                                print(name,":",b,'\n''pc:',b)
                                print('\033[30,1m'+"equal")
                                continue
                            elif(select3=="c" and ra.choice(list)=='s'):
                                print(name,":",c,'\n''pc:',c)
                                print('\033[30,1m'+"equal")
                                continue
                        
                            elif(select3=="c" and ra.choice(list)=='r'):
                                print(name,":",c,'\n''pc:',a)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                            elif(select3=="a" and ra.choice(list)=='p'):
                                print(name,":",a,'\n''pc:',b)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                            elif(select3=="b" and ra.choice(list)=='s'):
                                print(name,":",b,'\n''pc:',c)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                else:
                    table=[['name','point'],
                        [name,count1],
                        ['pc',count2]]
                    print(ta(table,tablefmt='fancy_grid'))
                    break
        #SINGLE 5 POINT
        elif select2==3:
            
            while True:
                if count1<5 and count2<5:
                            table1=[["select:"],
                            ['a)stone'],
                            ['b)paper'],
                            ['c)scissor']]
                            print(ta(table1,tablefmt='fancy_grid'))
                            select3=input('\033[33;1m'+'choice : ')
                            
                            if (select3=='a' and ra.choice(list)=='s'):
                                print(name,":",a,'\n'+'pc:',c)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                            elif (select3=='b' and ra.choice(list)=='r'):
                                print(name,":",b,'\n'+'pc:',a)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                            elif(select3=='c' and ra.choice(list)=='p'):
                                print(name,":",c,'\n'+'pc:',b)
                                print('\033[32;1m'+'hooray,',name,'is winer')
                                count1+=1
                                continue
                        
                        
                            elif(select3=="a" and ra.choice(list)=='r'):
                                print(name,":",a,'\n''pc:',a)
                                print('\033[30,1m'+"equal")
                                continue
                            elif(select3=="b" and ra.choice(list)=='p'):
                                print(name,":",b,'\n''pc:',b)
                                print('\033[30,1m'+"equal")
                                continue
                            elif(select3=="c" and ra.choice(list)=='s'):
                                print(name,":",c,'\n''pc:',c)
                                print('\033[30,1m'+"equal")
                                continue
                        
                            elif(select3=="c" and ra.choice(list)=='r'):
                                print(name,":",c,'\n''pc:',a)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                            elif(select3=="a" and ra.choice(list)=='p'):
                                print(name,":",a,'\n''pc:',b)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                            elif(select3=="b" and ra.choice(list)=='s'):
                                print(name,":",b,'\n''pc:',c)
                                print('\033[32;1m'+'hooray,pc is winer')
                                count2+=1
                                continue
                else:
                    table=[['name','point'],
                        [name,count1],
                        ['pc',count2]]
                    print(ta(table,tablefmt='fancy_grid'))
                    break