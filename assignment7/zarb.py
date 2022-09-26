
list=[]
p=''.join(list)
n=int(input("enter row: "))
m=int(input("enter column: "))
one=1
tow=1
for i in range(n):
    for i in range(m):
        c=one*tow
        tow+=1
        list.append(c)
        
    one+=1
    tow=1

for i in range(n):
        l=list[:m]
        if len(list)>0:
            del list[0:m]
            print(l)
        else:
            break        
