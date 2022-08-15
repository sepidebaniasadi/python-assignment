counter=0
win=0
loss=0
equal=0
sum=0

while counter<8:
    counter+=1
    print("enter rate",counter)
    rate=float(input("enter rate:"))
    sum=sum+rate
    if rate==3:
        win+=1
    elif rate==1:
      equal+=1
    elif rate==0:
        loss+1
    else:
        print("wrong")
        break
print ( "_____________________""\n","win= ",win,"\n","loss=",loss,"\n","equal= ",equal,"\n""finallyrate",sum)
        



