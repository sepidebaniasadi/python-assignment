passwrd=['8','2','1','3']
pass_p=['3','1','2','8']
count=1
while count<4:
    passu=list(input("enter password: "))
    if passwrd==passu:
          print('true')
          break
    elif passu==pass_p:
          print("we ringing police")
          break
    elif len(passu)>4:
        print("wrong you enter more digits")
        continue
    elif len(passu)<4:
            print("wrong you enter lower digits")
            continue
    else:
      print('wrong')
      count+=1
      
