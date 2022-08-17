number=float(input("enter number:"))
even=0
odd=0
while number>0:
     mod=number%10
     number=number//10
     if mod%2==0:
      even=even+1
     else:
      odd=odd+1
if even==odd:
    print("Your number has an equal number of even and odd digits")        
elif even>odd:
    print("Your number has more even digits")    
else:
    print("Your number has more odd digits")    


