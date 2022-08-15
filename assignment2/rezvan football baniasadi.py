counter=1
win1=0
win2=0
win3=0
win4=0
win5=0
fail1=0
fail2=0
fail3=0
fail4=0
fail5=0 
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
eq1=0
eq2=0
eq3=0
eq4=0
eq5=0
r1=0
r2=0
r3=0
r4=0
r5=0
while(counter<3):
    print("team1 with 2")
    rating1=int(float(input("enter rating of team1: ")))
    rating2=int(float(input("enter rating of team2: ")))
    if(rating1>rating2):
        win1=win1+1
        sum1=sum1+rating1
        fail2=fail2+1
        sum2=sum2+1 
        r1+=3
    elif rating1==rating2:
        eq1+=1
        eq2+=1
        r1+=1
        r2+=1

    else: 
        win2=win2+1
        sum2=sum2+rating2
        fail1=fail1+1
        sum1=sum1+rating2
        r2+=3
        counter=counter+1 
counter1_1=1
while(counter1_1<3):
    print("team1 with 3")
    rating1=int(float(input("enter rating of team1: ")))
    rating3=int(float(input("enter rating of team3: ")))
    if(rating1>rating3):
        win1=win1+1
        sum1=sum1+rating1
        fail3=fail3+1
        sum3=sum3+rating3
        r1+=3
    elif rating1==rating3:
        eq1+=1
        eq3+=1
        r1+=1
        r3+=1
    else:   
        win3=win3+1
        sum3=sum3+rating3
        fail1=fail1+1
        sum1=sum1+rating1
        r3+=3
        counter1_1+=1

counter1_3=1   
while(counter1_3<3) :
    print("team1 with 4")
    rating1=int(float(input("enter rating of team1: ")))
    rating4=int(float(input("enter rating of team4: ")))       
    if(rating1<rating4):
        fail1=fail1+1
        sum1=sum1+rating1 
        win4=win4+1    
        sum4=sum4+rating4
        r4+=1
    elif rating1==rating4:
        eq1+=1
        eq4+=1
        r4+=1
        r1+=1
    else:
        fail4=fail4+1
        sum4=sum4+rating4
        win1=win1+1    
        sum1=sum1+rating1
        r1+=3
        counter1_3+=1
counter1_4=1
while(counter1_4<3) :
    print("team1 with 5")
    rating1=int(float(input("enter rating of team1: ")))
    rating5=int(float(input("enter rating of team5: ")))       
    if(rating1<rating5):
        fail1=fail1+1
        sum1=sum1+rating1 
        win5=win5+1    
        sum5=sum5+rating5
        r5+=3
    elif rating1==rating5:
        eq1+=1
        eq5+=1
        r5+=1
        r1+=1
    else:
        fail5=fail5+1
        sum5=sum5+rating5
        win1=win1+1    
        sum1=sum1+rating1
        r1+=3
        counter1_4+=1       
counter2=1  
while(counter2<3) :
    print("team2 with 3")
    rating2=int(float(input("enter rating of team1: ")))
    rating3=int(float(input("enter rating of team2: ")))       
    if(rating3<rating2):
        fail3=fail3+1
        sum=sum3+rating3
        win2=win2+1    
        sum2=sum2+rating2
        r2+=3
    elif rating3==rating2:
        eq2+=1
        eq3+=1
        r2+=1
        r3+=1
    else:
        fail2=fail2+1
        sum2=sum2+rating2
        win3=win3+1    
        sum3=sum3+rating3
        r3+=3
        counter2+=1
counter2_1=1
while(counter2_1<3):
    print("team2 with 4")
    rating2=int(float(input("enter rating of team1: ")))
    rating4=int(float(input("enter rating of team2: ")))       
    if(rating4<rating2):
        fail4=fail4+1
        sum=sum4+rating4
        win2=win2+1    
        sum2=sum2+rating2
        r2+=3
    elif rating4==rating2:
        eq2+=1
        eq4+=1
        r4+=1
        r2+=1
    else:
        fail2=fail2+1
        sum2=sum2+rating2
        win4=win4+1    
        sum4=sum4+rating4
        r4+=3
        counter2_1+=1
counter2_2=1
while(counter2_2<3):
    print("team2 with 5")
    rating2=int(float(input("enter rating of team1: ")))
    rating5=int(float(input("enter rating of team2: ")))       
    if(rating5<rating2):
        fail5=fail5+1
        sum=sum5+rating5
        win2=win2+1    
        sum2=sum2+rating2
        r2+=3
    elif rating2==rating5:
        eq2+=1
        eq5+=1
        r2+=1
        r5+=1
    else:
        fail2+fail2+1
        sum2=sum2+rating2
        win5=win5+1    
        sum5=sum5+rating5
        r5+=3
        counter2_2+=1
counter3=1
while(counter3<3):
    print("team 4 with 3")
    rating4=int(float(input("enter rating of team4: ")))
    rating3=int(float(input("enter rating of team3: ")))
    if(rating3>rating4):
        win3=win3+1
        sum3=sum3+rating3
        fail4=fail4+1
        sum4=sum4+rating4
        r3+=3
    elif rating3==rating4:
        eq3+=1
        eq4+=1
        r4+=1
        r3+=1
    else:   
        win4=win4+1
        sum4=sum4+rating4
        fail3=fail3+1
        sum3=sum3+rating3
        r4+=3
        counter3=counter3+1
counter3_1=1
while(counter3_1<3):
    print("team 3 with 5")
    rating5=int(float(input("enter rating of team4: ")))
    rating3=int(float(input("enter rating of team3: ")))
    if(rating3>rating5):
        win3=win3+1
        sum3=sum3+rating3
        fail5=fail5+1
        sum5=sum5+rating5
        r3+=3
    elif rating3==rating5:
        eq5+=1
        eq3+=1
        r3+=1
        r5+=1
    else:   
        win5=win5+1
        sum5=sum5+rating5
        fail3=fail3+1
        sum3=sum3+rating3
        r5+=3
        counter3_1=counter3_1+1
counter4=1
while(counter4<3):
    print("team4 with 5")
    rating4=int(float(input("enter rating of team4: ")))
    rating5=int(float(input("enter rating of team5: ")))
    if(rating5>rating4):
        win5=win5+1
        sum5=sum5+rating5
        fail4=fail4+1
        sum4=sum4+rating4
        r5+=3
    elif rating1==rating2:
        eq4+=1
        eq5+=1
        r5==1
        r4+=1
    else:   
        fail5=fail5+1
        sum5=sum5+rating5
        win4=win4+1    
        sum4=sum4+rating4
        r4+=3
        counter4=counter4+1
print("____________________________________________________""\n""team1= ""\n""Number of football goals= "+sum1)
print("loss= "+fail1)
print("rate="+r1)
print("win +"+win1)
print("____________________________________________________""\n""team2= ""\n""Number of football goals= "+sum2)
print("loss= "+fail2)
print("rate="+r2)
print("win +"+win2)
print("____________________________________________________""\n""team3= ""\n""Number of football goals= "+sum3)
print("loss= "+fail3)
print("rate="+r3)
print("win +"+win3)
print("____________________________________________________""\n""team4= ""\n""Number of football goals= "+sum4)
print("loss= "+fail4)
print("rate="+r4)
print("win +"+win4)
print("____________________________________________________""\n""team5= ""\n""Number of football goals= "+sum5)
print("loss= "+fail5)
print("rate="+r5)
print("win +"+win5)
