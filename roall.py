import random
sum=0
roall=random.randint(1,6)
print(roall)
while(True ):   
    if roall<6:
        break
    sum+=roall
    if roall==6:
        for i in range (2):
            print("horay,you are lucky")
            roall=random.randint(1,6)
            print(roall)
            sum+=roall
            print("sum is= ",sum)
            if roall<6:
               break
            else:
                continue
    

    