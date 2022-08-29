#soodi motlaq
#list=[]
#listt=[]
#for i in range (10):
 #  list.append(num)
#for i in range(len(list)):
    #for j in range(0,len(list)-i-1):
        #if list[j]>list[j+1]:
            #list[j],list[j+1]=list[j+1],list[j]
            #c=True
    #if c==False:
       # break
#for i in range(len(list)):
   # listt.append(list[i])
#print('='*10,'sort','='*10,'\n',listt)


#SOODI
list=[]
listt=[]
for i in range (10):
    num=int(input(' enter num : '))
    list.append(num)
for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            c=True
    if c==False:
        break
for i in range(len(list)):
    listt.append(list[i])
print('='*10,'sort','='*10,'\n',listt)
