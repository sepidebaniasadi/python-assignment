n=int(input('enter your round: '))
list=[]
for i in range(n):
    name=input("enter name:")
    list.append(name)
    n=list.count(list[i])
    print(n,'=',list[i])

