# def taqsim (x,y):
#     ans=(x/y)
#     print(ans)
# def zard(x,y):
#     ans=(x*y)
#     print(ans)
# def jam(x,y):
#     ans=(x+y)
#     print(ans)
# def menha(x,y):
#     ans=(x-y)
#     print(ans)

list_op=[]
list_ans=[]
math_phrase=input("enter your math phrase: ")

a=math_phrase.split("*")
b=' '.join(a)
c=b.split("/")
d=' '.join(c)
e=d.split("+")
f=' '.join(e)
g=f.split("-")
h="".join(g)
list=h.split()


for mathematical in math_phrase:
   if mathematical=='/' or mathematical=='*' or mathematical=='+' or mathematical=='-':
        list_op.append(mathematical)

for i in range (len(list)-1):
       a="".join(list_op)
       m=a.find('/')
       
       if m!=-1:
        a=float(list[m])
        b=float(list[m+1])
        
        list.pop(m)
        list.insert(m,a/b)
        list.pop(m+1)
        list_op.pop(m)
       else:
        a="".join(list_op)
        m=a.find('*')
        if m!=-1:
            a=float(list[m])
            b=float(list[m+1])
            
            list.pop(m)
            list.insert(m,a*b)
            list.pop(m+1)
            list_op.pop(m)

    

        
for i in range (len(list)-1):
       a="".join(list_op)
       m=a.find('+')
       
       if m!=-1:
        a=float(list[m])
        b=float(list[m+1])
        
        list.pop(m)
        list.insert(m,a+b)
        list.pop(m+1)
        list_op.pop(m)
       else:
        a="".join(list_op)
        m=a.find('-')
        if m!=-1:
            a=float(list[m])
            b=float(list[m+1])
            
            list.pop(m)
            list.insert(m,a+b)
            list.pop(m+1)
            list_op.pop(m)

        

        

print(math_phrase,'=',list)
        

    