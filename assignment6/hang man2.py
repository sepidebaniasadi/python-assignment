
import random as ra
from colorama import Fore,Back,Style
from tabulate import tabulate
from pyfiglet import Figlet as p

F=p(font='standard')
d=0 
d1=0
d2=0
c=False
print(F.renderText('WELECOME''\n' 'TO''\n'' HANG MAN GAME'))
w_list=[]
show_list=[]
letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
name=(input(Fore.GREEN+"plz enter yout name ^_^: "+Style.RESET_ALL))
print(Fore.CYAN+"well,",Back.LIGHTMAGENTA_EX+name,Style.RESET_ALL+Fore.CYAN+" we have   category for this game:D"+Style.RESET_ALL)
list_animal_l1=['cat','cow','crab','deer','dog','pig']
list_animal_l2=['shark','tiger','wolf','zebra','chick','douck']
list_animal_l3=['puppy','dolphin','shrimp','rabbit','whale','crocodile']
list_irname_l1=['zahra','fatemeh','masoumeh','ali','mohamad','amir']
list_irname_l2=['hanieh','atefeh','sepideh','hossein','mahmood','mohsen']
list_irname_l3=['mohammad hossein','maral','davood','mohamad hassan','fatemeh zahra','nazanin']
list_fnames_l1=['sam','alex','eric','amy','angela','alis']
list_fnames_l2=['elika','barbara','pamela','varan','haman','ata']
list_fnames_l3=['patricia','rashel','solina','jalinos','eiliad','karanos']
list_IRfoodl1=['kabab','ash','gheimeh','soup','morgh']
list_IRfoodl2=['ghorme sabzi','koko sabzi','hot dog','adasi','bademjoon']
list_irfoodl3=['fesenjoon','baghali polo','makarani','mahi','mirza ghasemi']
list_ffoodl1=['omlet','pizza','Sushi','taco','pasta']
list_ffoodl2=['sashimi','hummud','Bacon','burger','pork','paella']
list_ffoodl3=['takoyaki','ramen','sukiyaki','tempura','kimvap']
list_irfilml1=['ch','motreb','ekhraji ha','del','tala']
list_irfilml2=['taik khal','sag band','asb','enferadi','dinamit']
list_irfilml3=['katiusha','meditarane','chahar angosht','ankaboot','rbe siah']
list_ffilml1=['days','drive','witches','fairy tale','venom']
list_ffilml2=['abigail','carter','rings','barbarians','the host']
list_ffilml3=['killer next door','before you','downfall','zombieland','the dragon pearl']
list_sporl1=['football','volleyball','basketball','baseball','ping pong']
list_sporl2=['taekwondo','wushu','wrestling','gymnastics','boxing']
list_sportl3=['sepak takra','track and field','swimming','javelin','weightlifting']
list_dressl1=['pants','dress','skirt','jeans','tshirt']
list_dressl2=['pajamas','scarf','sweater','uniform','vest']
list_dressl3=['blazer','jumper','crop top','swimsuit','gloves']
list_colorl1=['red','yellow','green','blue','black']
list_colorl2=['pink','orange','purpel','browen','gray']
list_colorl3=['musard','cyan','amethyst','emerald','beige']
list_fruit_1=['kiwi','banana','appel','melone','peach']
list_fruit_2=['avocado','orange','mulberry','pine appel','pear']
list_fruit_3=['mnago','grapes','strawberry','watermelon','cherry']

while True:
    table=[[Fore.GREEN+Back.LIGHTMAGENTA_EX+'1)hard'+Style.RESET_ALL],
    [Fore.GREEN+Back.LIGHTMAGENTA_EX+'2)easy'+Style.RESET_ALL]]
    print(tabulate(table,tablefmt='fancy_grid'))
    x=input(Fore.RED+'CHOICE:'+Style.RESET_ALL)
    if x=='1':

        table=[[Back.LIGHTMAGENTA_EX+'categorys'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'1)animals'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'2)IR names'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'3)Foreign names'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'4)IR foods'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'5)Foreign foods'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'6)IR films'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'7)Foreign film'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'8)fruits'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'9)sports'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'10)clothes'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'11)color'+Style.RESET_ALL]]
        print(tabulate(table,tablefmt='fancy_grid'))

        select2=int(input(Fore.RED+"choice: "+Style.RESET_ALL))

        print(Fore.LIGHTYELLOW_EX+Back.LIGHTMAGENTA_EX+name+Style.RESET_ALL+Fore.LIGHTYELLOW_EX+'you are choice',select2,'for category:D')
        if select2==1:
            
            for s in range(3):
                #level 1 animall

                if s==0:
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_animal_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower().lower()
                        
                                
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #animal 2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_animal_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)

                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_animal_l3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)

                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        elif select2==2:
            
            for s in range(3):
                #level 1 air name
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_irname_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                        
                            
                                    
                                    
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #irname 2
                elif s==1 and c==True:
                    print(F.renderText('level tow'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_irname_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break
                if s==2 and c==True:
                    
                    print(F.renderText('level three'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_irname_l3)
                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)

                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        elif select2==3:
            
            for s in range(3):
                #level 1 fname
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_fnames_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #f fname2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_fnames_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # fname3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_fnames_l3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==4:
            
            for s in range(3):
                #level 1 ir food1
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_IRfoodl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ir food2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_IRfoodl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # f irfood3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_irfoodl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==5:
            
            for s in range(3):
                #level 1 ffood
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_ffoodl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ffood2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_ffoodl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # ffood3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_ffoodl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==6:
            
            for s in range(3):
                #leveirfilml 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_irfilml1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ir film2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_irfilml2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # irfilm3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_irfilml3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #ffilm1
        elif select2==7:
            
            for s in range(3):
                #leveffilml 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_ffilml1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #f film2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_ffilml2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # ffilm3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_ffilml3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        #fruite
        elif select2==8:
            
            for s in range(3):
                #level1fruit 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_fruit_1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #fruit2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_fruit_2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # fruite3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_fruit_3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #sport1
        elif select2==9:
            
            for s in range(3):
                
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_sporl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #sport2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_sporl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # sport3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_sportl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #cloth
        elif select2==10:
            
            for s in range(3):
                
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_dressl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #cloth2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_dressl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # cloth3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_dressl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps^_^"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==11:
            
            for s in range(3):
                #level 1 air name
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_colorl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                        
                            
                                    
                                    
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #irname 2
                elif s==1 and c==True:
                    print(F.renderText('level tow'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_colorl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break
                if s==2 and c==True:
                    
                    print(F.renderText('level three'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_colorl3)
                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)

                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break


                            
        if c==False:
                ex=input("Would you like to try again?yes/no...")
                if ex.lower()=='yes':
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    s=0
                    d=0
                    d1=0
                    d2=0
                    show_list.clear()
                    w_list.clear()
                    continue
                elif ex.lower()=='no':
                    print("BYE BYE^_^")
                    break
                else:
                    "wrong"
                    break
        
                             

                ######################################################################################################################################################################################
                ##########################################################easyyyyyyyyyyyyyyyyyyyyyy#######################################################################################################################
                #########################################################################################################################################################################################################
    elif x=='2':
        table=[[Back.LIGHTMAGENTA_EX+'categorys'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'1)animals'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'2)IR names'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'3)Foreign names'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'4)IR foods'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'5)Foreign foods'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'6)IR films'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'7)Foreign film'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'8)fruits'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'9)sports'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'10)clothes'+Style.RESET_ALL],
        [Fore.GREEN+Back.LIGHTMAGENTA_EX+'11)colors'+Style.RESET_ALL]]
        print(tabulate(table,tablefmt='fancy_grid'))

        select2=int(input(Fore.RED+"choice: "+Style.RESET_ALL))

        print(Fore.LIGHTYELLOW_EX+Back.LIGHTMAGENTA_EX+name+Style.RESET_ALL+Fore.LIGHTYELLOW_EX+'you are choice',select2,'for category:D')
        if select2==1:
            
            for s in range(3):
                #level 1 animall

                if s==0:
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_animal_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(list_animal_l1)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)

                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)


                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #animal 2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_animal_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_animal_l2)+Style.RESET_ALL)

                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)

                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break
                           # animal3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_animal_l3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_animal_l3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)

                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        elif select2==2:
            
            for s in range(3):
                #level 1 air name
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_irname_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irname_l1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                        
                            
                                    
                                    
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #irname 2
                elif s==1 and c==True:
                    print(F.renderText('level tow'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_irname_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irname_l2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break
                            #irname3
                elif s==2 and c==True:
                    
                    print(F.renderText('level three'))
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    
                    finall_w=ra.choice(list_irname_l3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irname_l3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        elif select2==3:
            
            for s in range(3):
                #level 1 fname
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_fnames_l1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fnames_l1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #f fname2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_fnames_l2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fnames_l2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # fname3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_fnames_l3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fnames_l3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==4:
            
            for s in range(3):
                #level 1 ir food1
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_IRfoodl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_IRfoodl1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ir food2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_IRfoodl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_IRfoodl2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # f irfood3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_irfoodl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irfoodl3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==5:
            
            for s in range(3):
                #level 1 ffood
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_ffoodl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffoodl1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ffood2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_ffoodl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffoodl2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # ffood3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_ffoodl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffoodl3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==6:
            
            for s in range(3):
                #leveirfilml 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_irfilml1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irfilml1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #ir film2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_irfilml2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irfilml2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # irfilm3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_irfilml3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_irfilml3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #ffilm1
        elif select2==7:
            
            for s in range(3):
                #leveffilml 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_ffilml1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffilml1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #f film2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_ffilml2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffilml2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # ffilm3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_ffilml3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_ffilml3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break

        #fruite
        elif select2==8:
            
            for s in range(3):
                #level1fruit 
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_fruit_1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fruit_1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #fruit2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_fruit_2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fruit_2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # fruite3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_fruit_3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_fruit_3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #sport1
        elif select2==9:
            
            for s in range(3):
                
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_sporl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_sporl1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #sport2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_sporl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_sporl2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # sport3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_sportl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_sportl3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        #cloth
        elif select2==10:
            
            for s in range(3):
                
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_dressl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_dressl1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #cloth2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_dressl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_dressl2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # cloth3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_dressl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_dressl3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps^_^"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        elif select2==11:
            
            for s in range(3):
                
                if s==0:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level one'))
                    
                    finall_w=ra.choice(list_colorl1)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(list_colorl1)+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                d==0
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                else:
                                    print(Fore.RED+"sorry ,",name,"You haven't made it to the next step:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    break
                    #cloth2
                elif s==1 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level tow'))
                    
                    finall_w=ra.choice(list_colorl2)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_colorl2)+Style.RESET_ALL)
                        if d1<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d1+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    
                                    w_list.clear()
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through one steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    show_list.clear()
                                break

            # cloth3
                if s==2 and c==True:
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    print(F.renderText('level three'))
                    
                    finall_w=ra.choice(list_colorl3)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                    print(Fore.CYAN+l+Style.RESET_ALL)
            
                    while True:
                        
                        print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        print(Fore.LIGHTRED_EX+"_".join(                                                   list_colorl3)+Style.RESET_ALL)
                        if d2<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                c=True
                                show_list.clear()
                                w_list.clear()
                                break
                            else:
                                
                                letter=input(Fore.LIGHTMAGENTA_EX+"letter: "+Style.RESET_ALL).lower()
                        
                                if letterlist.find(letter)==-1:
                                    print('wrong')
                                    continue
                                else:
                                    letterlist=letterlist.split("*")
                                    letterlist.remove(letter)
                                    letterlist='*'.join(letterlist)
                                if finall_w.find(letter)==-1:
                                    w_list.append(letter)
                                    d2+=1
                                    
                                else:
                                    for i in range(len(finall_w)):
                                        if finall_w[i]==letter:
                                            show_list[i]=letter.lower()
                                        else:
                                            continue      
                                l2="".join(show_list)
                                l3="".join(w_list)
                                print(Fore.CYAN+l2,'\n'+l3+Style.RESET_ALL)
                                
                        else:
                                if l2==finall_w:
                                    print(Fore.GREEN+"hooray,",name,"you were able to go through all the steps^_^"'\n''bye bye:D'+Style.RESET_ALL)
                                    c=True
                                    show_list.clear()
                                    w_list.clear()
                                    
                                else:
                                    print(Fore.RED+"sorry ,",name,"you were able to go through two steps:("'\n''bye bye^_^'+Style.RESET_ALL)
                                    c=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                break
        if c==False:
                ex=input("Would you like to try again?yes/no...")
                if ex.lower()=='yes':
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    s=0
                    d=0
                    d1=0
                    d2=0
                    show_list.clear()
                    w_list.clear()
                    continue
                elif ex.lower()=='no':
                    print("BYE BYE^_^")
                    break
                else:
                    "wrong"
                    break

