from ast import Break


username="sepidehbaniasadi"
password='400154126'
count=0
print("You can only enter your password three times")
while(count<3):
    username_1=input("please enter your username : ")
    password_1=input("please enter your password : ")
    if(username_1==username and password_1==password):
       print("you are varified")
       break
    else:
     print("wrong")   

    count=count+1 
if(count>2):
    print("access denied")


