import random
time=int(input("size of your random list : "))
list=[]
for i in range (time):
    num=random.randint(0,99)
    list.append(num)
print("="*10,'\n''your list =',list)
