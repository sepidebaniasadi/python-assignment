length=(float(input("enter your length with metr: ")))
wieght=(float(input('enter your wieght with kg: ')))
BMI=(wieght/(length**2))
if BMI>=16 and BMI<18.5:
    print(" your BMI is: ", BMI,'/n'"body wiegth deficit")
elif BMI>=18.5 and BMI<24:
    print(" your BMI is: ", BMI,'/n'"normal")
elif BMI>=24 and BMI<30:
    print(" your BMI is: ", BMI,'/n'"wieght over")  
elif BMI>=30 and BMI<35:
    print(" your BMI is: ", BMI,'/n'"obesity first degree")     
elif BMI>=35 and BMI<40:
    print(" your BMI is: ", BMI,'/n'"obesity second degree")  
elif BMI>=40:
    print(" your BMI is: ", BMI,'/n'"obesity third degree")
else:
    print("This interval was unpredictable.")

