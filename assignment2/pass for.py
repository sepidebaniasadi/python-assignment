username="sepidehbaniasadi"
password='400154126'
print("You can only enter your password three times")
for i in range(3):
    username_1=input("enter  your user: ")
    password_1=input("enter your pass: ")
    if username==username_1 and password_1==password:
        print("true")
        break
    else:
        print("wrong")
