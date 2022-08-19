hour=list(input("enter hour:"))
minute=list(input("enter minute: "))
secondes=list(input('enter secondes'))
print("------------"'\n''select your convert: ''\n''1)hour--->secondes''\n''2)secondes--->hour')
select=int(input("select:"))
sumh=[]
sumh=int(hour[0])+int(hour[1])
secondes_h=sumh*3600
sumM=[]
sumM=int(minute[0])+int(minute[1])
secondes_m=sumM*60
sumS=[]
sumS=int(secondes[0])+int(secondes[1])
hour_s=sumS/3600
hour_m=sumM/60
if select==1:
    sum=secondes_h+secondes_m+sumS
    print("hour --->secondes is : ",sum)
elif select==2:
    sum2=hour+hour_m+hour_s
    print("secondes--->hour is : ",sum2)
else:
    print("wrong")



