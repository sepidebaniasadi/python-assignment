import random
answer_pc=random.randint(0,99)
answere=99
answers=0
counter=1
print(answer_pc)


while True:
   
    print('1)horaaay,it is true''\n''2)no my number is bigger''\n''3)no my number is lower')
    
    useranswer = int(input())
    if useranswer==1:
        print("you can geuss after",counter,'time')
        break
    elif useranswer==2:
        answers=answer_pc
        answer_pc=random.randint(answers+1,answere-1)
        counter+=1
        print(answers)
    elif useranswer==3:
        answere=answer_pc
        answer_pc=random.randint(answers+1,answere-1)
        counter+=1
        print(answere)
    else:
        print("wrong")

    


