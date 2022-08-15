number=float(input("enter number:"))
if number%7==0:
    print(number,"is multiple seven.")
else:
    next= number + (7 - number % 7)
    print(number,"is not multiple seven next number then multiple seven  is",next)
   