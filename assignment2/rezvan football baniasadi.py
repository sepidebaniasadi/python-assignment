
win1 =0
win2 = 0
win3 = 0
win4 = 0
win5 = 0

fail1 = 0
fail2 = 0
fail3 = 0
fail4 = 0
fail5 = 0 

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

eq1 = 0
eq2 = 0
eq3 = 0
eq4 = 0
eq5 = 0

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

for i in range(2):
    print("team 1 with 2")
    Goal1=int(float(input("enter Goal of team 1: ")))
    Goal2=int(float(input("enter Goal of team 2: ")))
    if(Goal1>Goal2):
        win1=win1+1
        sum1=sum1+Goal1
        fail2=fail2+1
        sum2=sum2+1 
        r1+=3
    elif Goal1==Goal2:
        eq1+=1
        eq2+=1
        r1+=1
        r2+=1
    elif(Goal2>Goal1):
        win2=win2+1
        sum2=sum2+Goal2
        fail1=fail1+1
        sum1=sum1+Goal2
        r2+=3

    else: 
        win2=win2+1
        sum2=sum2+Goal2
        fail1=fail1+1
        sum1=sum1+Goal2
        r2+=3
      

for i in range(2):
    print("team 1 with 3")
    Goal1=int(float(input("enter Goal of team 1: ")))
    Goal3=int(float(input("enter Goal of team 3: ")))
if(Goal1>Goal3):
    win1=win1+1
    sum1=sum1+Goal1
    fail3=fail3+1
    sum3=sum3+Goal3
    r1+=3
elif Goal1==Goal3:
    eq1+=1
    eq3+=1
    r1+=1
    r3+=1

else:   
    win3=win3+1
    sum3=sum3+Goal3
    fail1=fail1+1
    sum1=sum1+Goal1
    r3+=3

  

for i in range(2):
    print("team1 with 4")
    Goal1=int(float(input("enter Goal of team 1: ")))
    Goal4=int(float(input("enter Goal of team 4: ")))       
if(Goal1<Goal4):
    fail1=fail1+1
    sum1=sum1+Goal1 
    win4=win4+1    
    sum4=sum4+Goal4
    r4+=1
elif Goal1==Goal4:
    eq1+=1
    eq4+=1
    r4+=1
    r1+=1
else:
    fail4=fail4+1
    sum4=sum4+Goal4
    win1=win1+1    
    sum1=sum1+Goal1
    r1+=3

for i in range(2):
    print("team 1 with 5")
    Goal1=int(float(input("enter Goal of team 1: ")))
    Goal5=int(float(input("enter Goal of team 5: ")))       
if(Goal1<Goal5):
    fail1=fail1+1
    sum1=sum1+Goal1 
    win5=win5+1    
    sum5=sum5+Goal5
    r5+=3
elif Goal1==Goal5:
    eq1+=1
    eq5+=1
    r5+=1
    r1+=1
else:
    fail5=fail5+1
    sum5=sum5+Goal5
    win1=win1+1    
    sum1=sum1+Goal1
    r1+=3
for i in range(2):
    print("team 2 with 3")
    Goal2=int(float(input("enter Goal of team 3: ")))
    Goal1=int(float(input("enter Goal of team 1: ")))       
if(Goal3<Goal2):
    fail3=fail3+1
    sum=sum3+Goal3
    win2=win2+1    
    sum2=sum2+Goal2
    r2+=3
elif Goal3==Goal2:
    eq2+=1
    eq3+=1
    r4+=1
    r2+=1
else:
    fail2=fail2+1
    sum2=sum2+Goal2
    win3=win3+1    
    sum3=sum3+Goal3
    r3+=3

for i in range(2):
    print("team 2 with 4")
    Goal2=int(float(input("enter Goal of team 2: ")))
    Goal4=int(float(input("enter Goal of team 4: ")))       
if(Goal4<Goal2):
    fail4=fail4+1
    sum=sum4+Goal4
    win2=win2+1    
    sum2=sum2+Goal2
    r2+=3
elif Goal4==Goal2:
    eq2+=1
    eq4+=1
    r4+=1
    r2+=1
else:
    fail2=fail2+1
    sum2=sum2+Goal2
    win4=win4+1    
    sum4=sum4+Goal4
    r4+=3
for i in range(2):
    print("team 2 with 5")
    Goal2=int(float(input("enter Goal of team 2: ")))
    Goal5=int(float(input("enter Goal of team 5: ")))       
if(Goal5<Goal2):
    fail5=fail5+1
    sum5=sum5+Goal5
    win2=win2+1    
    sum2=sum2+Goal2
    r2+=3
elif Goal5==Goal2:
    eq2+=1
    eq5+=1
    r5+=1
    r2+=1
else:
    fail2=fail2+1
    sum2=sum2+Goal2
    win5=win5+1    
    sum5=sum5+1
    r5+=1
for i in range(2):
    print("team 3 with 4")
    Goal3=int(float(input("enter Goal of team 3: ")))
    Goal4=int(float(input("enter Goal of team 4: ")))       
if(Goal3<Goal4):
    fail3=fail3+1
    sum3=sum3+Goal3
    win4=win4+1    
    sum4=sum4+Goal4
    r4+=3
elif Goal4==Goal3:
    eq3+=1
    eq4+=1
    r3+=1
    r4+=1
else:
    fail4=fail4+1
    sum4=sum4+Goal4
    win3=win3+1    
    sum3=sum3+Goal4
    r3+=3

for i in range(2):
    print("team 3 with 5")
    Goal3=int(float(input("enter Goal of team 3: ")))
    Goal5=int(float(input("enter Goal of team 5: ")))       
if(Goal3<Goal5):
    fail3=fail3+1
    sum3=sum3+Goal3
    win5=win5+1   
    sum5=sum5+Goal5
    r5+=3
elif Goal5==Goal3:
    eq3+=1
    eq5+=1
    r3+=1
    r5+=1
else:
    fail5=fail5+1
    sum5=sum5+Goal5
    win3=win3+1    
    sum3=sum3+Goal4
    r3+=3

for i in range(2):
    print("team 4 with 5")
    Goal4=int(float(input("enter Goal of team 2: ")))
    Goal5=int(float(input("enter Goal of team 5: ")))       
if(Goal5<Goal4):
    fail5=fail5+1
    sum5=sum5+Goal5
    win4=win4+1    
    sum4=sum4+Goal4
    r4+=3
elif Goal5==Goal4:
    eq4+=1
    eq5+=1
    r5+=1
    r4+=1
else:
    fail4=fail4+1
    sum4=sum4+Goal4
    win5=win5+1    
    sum5=sum5+1
    r5+=1
print("____________________________________________________""\n""team1= ""\n""Number of football goals= " ,(sum1),"\n""win=",(win1),"\n","loss= ",fail1,'\n''eqaul=',eq1,'\n''rate= ',r1)
print("____________________________________________________""\n""team2= ""\n""Number of football goals= " ,(sum2),"\n""win=",(win2),"\n","loss= ",fail2,'\n''eqaul=',eq2,'\n''rate= ',r2)
print("____________________________________________________""\n""team3= ""\n""Number of football goals= " ,(sum3),"\n""win=",(win3),"\n","loss= ",fail3,'\n''eqaul=',eq3,'\n''rate= ',r3)
print("____________________________________________________""\n""team4= ""\n""Number of football goals= " ,(sum4),"\n""win=",(win4),"\n","loss= ",fail4,'\n''eqaul=',eq4,'\n''rate= ',r4)
print("____________________________________________________""\n""team5= ""\n""Number of football goals= " ,(sum5),"\n""win=",(win5),"\n","loss= ",fail5,'\n''eqaul=',eq5,'\n''rate= ',r5)
