from matplotlib import style
from tabulate import tabulate as ta
from colorama import Fore,Back,Style
while True:
    fng_eng_dict={'man':'me','hast':['is','are'],'daneshgah':'university','jangal':'forest','mahi':"fish",
    "darya":"see","ab":'water','mashin':'car','tasadof':'accident','moalem':'teacher','modir':"principale",'sib':"apple","daneshjoo":'student','ghaza':"food",
    "shal":"scarf","joorab":"socks","tishert":"t_shirt","hastam":'am','go':'go','shena':'swimm','stakhr':'pool','toop':'ball','kooh':'mountain','bagh':'garden','maman':'mom',
    'baba':['dad',"father"],'dadash':'brother','gol':'flower','salam':'hi'}
    table=[['1)fingelish to english'],
    ['2)fingelish to persian'],
    ['3)exit']]
    print(ta(table,tablefmt='fancy_grid'))
    i=int(input('chose your type?1 or 2 or 3? '))
    if i==1:
        jomle=(input('jomle khod ra vared konid: '))
        kalammat=jomle.split()
        javab=''
        for kalame in kalammat:
            if kalame in fng_eng_dict:
                javab=javab+ '  '+Fore.RED+(fng_eng_dict[kalame]).upper()+Style.RESET_ALL
            else:
                javab=(javab+'   '+kalame)
        print(javab.strip())
    elif i==2:
        eng_fng_dict=per_eng_dict={'me':'man','is':'hast','university':'daneshgah','forest':'jangal',"fish":'mahi',
        "see":"darya",'water':"ab",'car':'mashin','accident':'tasadof','teacher':'moalem',"principale":'modir',"apple":'sib','student':"daneshjoo","food":'ghaza',
        "scarf":"shal","socks":"joorab","t_shirt":"tishert",'am':"hastam",'go':'go','swimm':'shena','pool':'stakhr','ball':'toop','mountain':'kooh','garden':'bagh','mom':'maman',
        'dad':'baba','brother':'dadash','flower':'gol','hi':'salam'}
        jomle=((input('enter your sentence...')))
        kalammat=jomle.split()
        javab=''
        for kalame in kalammat:
            if kalame in per_eng_dict:
                javab=javab+ '  '+Fore.RED+per_eng_dict[kalame].upper()+Style.RESET_ALL
            else:
                javab=javab+'   '+kalame
        print(javab.strip())
    elif i==3:
        break
    else:
        print("wrong")
        continue
