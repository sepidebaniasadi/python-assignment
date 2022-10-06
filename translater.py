import arabic_reshaper
from bidi.algorithm import get_display
from tabulate import tabulate as ta
while True:
    per_eng_dict={'سلام':'hi','من':'me','هست':['is','are'],'کامپیوتر':['computer','pc'],'دانشگاه':'university','جنگل':'forest','ماهی':"fish",
    "دریا":"see","اب":'water','ماشین':'car','تصادف':'accident','معلم':'teacher','مدیر':"principale",'سیب':"apple","دانشجو":'student','غذا':"food",
    "شال":"scarf","جوراب":"socks","تیشرت":"t_shirt","هستم":'am','برو':'go','شنا':'swimm','استخر':'pool','توپ':'ball','کوه':'mountain','باغ':'garden','مامان':'mom','خواهر':'sister',
    'بابا':['dad',"father"],'داداش':'brother','گل':'flower'}
    table=[['1)persian to english'],
    ['2)english to persian'],
    ['3)exit']]
    print(ta(table,tablefmt='fancy_grid'))
    i=int(input('chose your type?1 or 2 or 3? '))
    if i==1:
        print(get_display(arabic_reshaper.reshape('جمله خود را وارد کنید ')))
        jomle=(input())
        print('\n'+(get_display(arabic_reshaper.reshape(jomle))))
        kalammat=jomle.split()
        javab=''
        for kalame in kalammat:
            if kalame in per_eng_dict:
                javab=get_display(arabic_reshaper.reshape(javab))+ '  '+(per_eng_dict[kalame]).upper()
            else:
                javab=get_display(arabic_reshaper.reshape(javab+'   '+kalame))
        print(javab.strip())
    elif i==2:
        per_eng_dict=per_eng_dict={'me':'من','is':'هست','computer':'کامپیوتر','university':'دانشگاه','forest':'جنگل',"fish":'ماهی',
        "see":"دریا",'water':"دریا",'car':'ماشین','accident':'تصادف','teacher':'معلم',"principale":'مدیر',"apple":'سیب','student':"دانشجو","food":'غذا',
        "scarf":"شال","socks":"جوراب","t_shirt":"تیشرت",'am':"هستم",'go':'برو','swimm':'شنا','pool':'استخر','ball':'توپ','mountain':'کوه','garden':'باغ','mom':'مامان','sister':'خواهر',
        'dad':'بابا','brother':'داداش','flower':'گل'}
        jomle=((input('enter your sentence...')))
        kalammat=jomle.split()
        javab=''
        for kalame in kalammat:
            if kalame in per_eng_dict:
                javab=javab+ '  '+per_eng_dict[kalame]
            else:
                javab=javab+'   '+kalame
        print(get_display(arabic_reshaper.reshape(javab.strip())))
    elif i==3:
        break
    else:
        print("wrong")
        continue
