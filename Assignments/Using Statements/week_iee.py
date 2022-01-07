# Q5.Write a python program, which will accept numer of a week and display it's name. #HW
# using if...elif...else
# week_iee.py

a=int(input("Enter Week Number : "))
if a==0:
    print("Week Numbers are from 1 to 7")
elif a<0:
    print("Enter Week in Positive Number From 1 to 7")
elif a==1:
    print("SUNDAY")
elif a==2:
    print("MONDAY")
elif a==3:
    print("WEDNESDAY")
elif a==4:
    print("THURSDAY")
elif a==5:
    print("FRIDAY")
elif a==6:
    print("SATURDAY")
elif a==7:
    print("SUNDAY")
else:
    print("Enter Valid Week Number")
    
# Using Simple way with Dictionary
week={1:"SUNDAY", 2:"MONDAY", 3:"TUESDAY", 4:"WEDNESDAY", 5:"THURSDAY", 6:"FRIDAY", 7:"SATURDAY"}
a=week.get(int(input("Enter Week Number : ")))
if a==None:
    print("You Enter Wrong Week Number, Please Enter correct Week Number b/w 1 to 7")
else:
    print(a)
