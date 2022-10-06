
def color(i):
    while True:
        color=(input("enter your color and when your color ended plz enter -1: "))
        if color!='-1':
            if i==1:
                list.append(color)
            else:
                list2.append(color)
                continue
        else:
            break
    if i==1:
        return(tuple(list))
    else:
        return(tuple(list2))
# def end(first,sec):
    # for color in first:
        # if color not in sec:
            # list3.append(color)
    # print(list3)
def end (first , sec):
    for color in first:
        str_sec=''.join(sec)
        if str_sec.find(color)==-1:
            list3.append(color)
    print(list3)


#both of them is true(end)
        


list=[]
list2=[]
list3=[]
i=1
first=color(i)
print('second one')
list.clear
i=2
sec=color(i)

print('first one: ',first)
print('second one:',sec)
end(first,sec)


