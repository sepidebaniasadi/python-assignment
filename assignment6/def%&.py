
# def dollara(m,n):
#     for i in range(n):
#         if i%2==0:  
#             print("$&"*m)
            
            
            
#         else:
#             print("&$"*m)
            
            
           

# n=int(input("Number of rows: "))
# m=int(input("Number of columns: "))
# print(dollara(m,n))

def dollara(m,n):
    for i in range(n):
        if i%2==0: 
            if m%2==0: 
              o=int(m/2)
              print('$&'*o)
            else:
                o=int(m/2)+1
                t=('$&'*o)
                print(t[:-1])

            
        else:
            if m%2==0:
                o=int(m/2)
                print("&$"*o)
            else:
                o=int(m/2)+1
                h=("&$"*o)
                print(h[:-1])
                   
           

n=int(input("Number of rows: "))
m=int(input("Number of columns: "))
print(dollara(m,n))
