from tempfile import TemporaryDirectory


number=int(input("enter number please enter a number that has six digit:"))
digit5=(number%100000  )//10000
digit2=(number%100)//10
sum=digit5+digit2
print(sum)
