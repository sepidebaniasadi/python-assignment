list=[]
c=True
for i in range (10):
    num=float(input("enter num: "))
    list.append(num)
for i in range(len(list)-1):
    if list[i]<list[i+1] or list[i+1]>list[i]:
        c=True
        continue
    else :
        c=False
        break
if c==True:
    print('yes')
elif c==False:
    print('no')
