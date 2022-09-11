
def dollara(m,n):
    for i in range(n):
        if i%2==0:  
            return("$&"*m)
            
        else:
            return("&$"*m)
           

n=int(input("Number of rows: "))
m=int(input("Number of columns: "))
print(dollara(m,n))
