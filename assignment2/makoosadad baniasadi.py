number=(int(input("enter a number: ")))
firstnum=number
reverse=0
while(number>0): 
    temp=number%10
    reverse=((reverse*10)+temp)
    number=number//10
if firstnum==reverse:
    print( reverse,"matchwith your first number")
else:
    print(reverse,"don't match with your first number")
