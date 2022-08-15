temperture=int(float(input("enter temprrture: ")))
space="                "
space1="       "
print("Please select one of the conversions below for the entered temperature""\n"" __________________""\n""|",space,"|""\n""|""1)c---->f",space1,"|""\n""|",space,"|""\n""|""2)f---->c",space1,"|""\n""|",space,"|""\n""|""3)k---->f",space1,"|""\n""|",space,"|""\n""|""4)f---->k",space1,"|""\n""|",space,"|""\n""|""5)c---->k",space1,"|""\n""|",space,"|""\n""|""6)k---->c",space1,"|","\n""|""__________________""|")
choose=int(float(input("Which one do you choose? ")))
if choose==1:
  farenheit=temperture(9/5)+32
  print("your tempercher with conversion is: ",farenheit,"farenheit")
elif choose==2:
    celsius=(temperture-32)*(5/9)
    print("your tempercher with conversion is: ",celsius,"celsius")
elif choose==3:
    farenheit=(temperture-273.15)*(5/9)+32
    print("your tempercher with conversion is: ",farenheit,"farenheit")
elif choose==4:
    kelvin=(temperture-32)*(5/9)+273.15
    print("your tempercher with conversion is: ",kelvin,"kelvin")
elif choose==5:
    kelvin=(temperture+273.15)
    print("your tempercher with conversion is: ",kelvin,"kelvin")
elif choose==6:
    celsius=(temperture-273.15)
    print("your tempercher with conversion is: ",celsius,"celsius")