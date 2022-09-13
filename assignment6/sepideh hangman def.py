
from codecs import namereplace_errors
from operator import iconcat
import random as ra
from colorama import Fore,Back,Style
from tabulate import tabulate
from pyfiglet import Figlet as p
F=p(font='standard')
I=False
w_list=[]
show_list=[]
def hardoreasy():
    table=[[Fore.GREEN+Back.LIGHTMAGENTA_EX+'1)hard'+Style.RESET_ALL],
    [Fore.GREEN+Back.LIGHTMAGENTA_EX+'2)easy'+Style.RESET_ALL]]
    print(tabulate(table,tablefmt='fancy_grid'))
def catg():
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
        
def level1_h(list, name,d,x):
                    

                    d=0 
                    letterlist='a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z'
                    finall_w=ra.choice(list)

                    for i in range(len(finall_w)):
                            show_list.append("_")
                            l=' '.join(show_list)
                            
                    print(Fore.CYAN+l+Style.RESET_ALL)
                    
            
                    while True:
                       
                        
                        I=False
                        if x=='1':
                            print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        elif x=='2':
                            print(Fore.LIGHTRED_EX+"_".join(list)+Style.RESET_ALL)
                            print(Fore.LIGHTRED_EX+letterlist+Style.RESET_ALL)
                        if d<len(show_list) :
                            if finall_w=="".join(show_list):
                                print(Fore.GREEN+"hooray,",name,"You've made it to the next step^_^"+Style.RESET_ALL)
                                I=True
                                
                                show_list.clear()
                                w_list.clear()
                                d==0
                                return(I)
                                
                                
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
                                    I=True
                                    show_list.clear()
                                    w_list.clear()
                                    d==0
                                    return(I)
                                else:
                                    print(Fore.RED+"sorry ,",name,"You have'nt made it to the next step:("+Style.RESET_ALL)
                                    I=False
                                    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTBLUE_EX+"answer was "+finall_w+Style.RESET_ALL)
                                    
                                    show_list.clear()
                                    w_list.clear()
                                    return(I)
                                    
                                    
def exit(ex,d):
                c=True
                if ex.lower()=='yes':
                    d=d
                    show_list.clear()
                    w_list.clear()
                    c=True
                    return(c)
                elif ex.lower()=='no':
                  c=False
                  return(c)
                else:
                    print("wrong")
def run(select2,name):
    
    print(Fore.LIGHTYELLOW_EX+Back.LIGHTMAGENTA_EX+name+Style.RESET_ALL+Fore.LIGHTYELLOW_EX+'you are choice',select2,'for category:D')
    I=False
    while True:
            for s in range(3):
                if s==0:
                    print(F.renderText('level one'))
                    list=list1[select2-1]
                    
                    d=0
                    I=(level1_h(list, name,d,x))
                    
                    
                elif s==1 and I==True:
                    print(F.renderText('level two'))
                    d2=0
                    d=d2
                    list=list2[select2-1]
                    I=(level1_h(list, name,d,x))    
                    
                     
                elif  s==2 and I==True:
                    print(F.renderText('level three'))
                    d3=0
                    d=d3
                    list=list3[select2-1]
                    I=(level1_h(list, name,d,x))
                    if I==False:
                                ex=input("Would you like to try again?yes/no...")
                                exit(ex,d) 
                                if exit(ex,d)==False:
                                    print("bye bye^_^")
                                    break
                    

            


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
list1=[list_animal_l1,list_irname_l1,list_fnames_l1,list_IRfoodl1,list_ffoodl1,list_irfilml1,list_ffilml1,list_fruit_1,list_sporl1,list_dressl1,list_colorl1]
list2=[list_animal_l2,list_irname_l2,list_fnames_l2,list_IRfoodl2,list_ffoodl2,list_irfilml2,list_ffilml2,list_fruit_2,list_sporl2,list_dressl2,list_colorl2]
list3=[list_animal_l3,list_irname_l3,list_fnames_l3,list_irfoodl3,list_ffoodl3,list_irfilml3,list_ffilml3,list_fruit_3,list_sportl3,list_dressl3,list_colorl3]
print(F.renderText('WELECOME''\n' 'TO''\n'' HANG MAN GAME'))
name=(input(Fore.GREEN+"plz enter your name ^_^: "+Style.RESET_ALL))
hardoreasy()
x=input(Fore.RED+'CHOICE:'+Style.RESET_ALL)
    
if x=='1':
    catg()
    select2=int(input(Fore.RED+"choice: "+Style.RESET_ALL))
    
    run(select2,name)
elif x=='2':
    catg()
    select2=int(input(Fore.RED+"choice: "+Style.RESET_ALL))
    run(select2,name)
    

    
    
    
    




