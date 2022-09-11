
def dollara(m,n):
    for i in range(n):
        if i%2==0:  
            print=("$&"*m)
            
            
            
        else:
            print=("&$"*m)
            
            
           

n=int(input("Number of rows: "))
m=int(input("Number of columns: "))
print(dollara(m,n))
