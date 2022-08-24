number = int(input("please Enter integer number: "))
factorial = number
for i in range(1,number-1):
    factorial = factorial / i
    if factorial==1:
        c=True
        break
    else:
        c=False
if c==True:
    print("yes")
else:
    print('no')
