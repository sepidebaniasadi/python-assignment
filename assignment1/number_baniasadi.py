from tempfile import TemporaryDirectory


number=int(input("enter number please enter a number that has more than one digit:"))
reverse=0
while number > 0:
  temp=number%10
  reverse=(reverse*10)+temp
  number=number//10
final=(reverse%100  )//10
print(final)