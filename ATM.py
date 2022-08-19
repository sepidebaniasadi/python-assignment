passwrd=['8','2','1','3']
pasu=[]
pass_p=['3','1','2','8']
for i in range(3):
    for i in range(4):
       pass_u=input("enter your passwordone by one digit: ")
       pasu.append(pass_u)
    if passwrd==pasu:
          print('true')
          break
    elif pasu==pass_p:
          print("we ringing police")
    else:
            print('wrong')
            continue
    




