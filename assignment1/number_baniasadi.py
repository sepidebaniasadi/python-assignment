from tempfile import TemporaryDirectory


number=int(input("enter number please enter a number that has more than one digit:"))
reverse=0
while number > 0:
  temp=number%10
  reverse=(reverse*10)+temp
  number=number//10
digit5=(reverse%100000  )//10000
digit2=(reverse%100)//10
sum=digit5+digit2
print(sum)
