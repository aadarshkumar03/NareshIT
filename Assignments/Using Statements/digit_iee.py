# Q4.Write a python program, which will accept any digit and print it's name. #CW
# Using if...elif...else
# digit_iee.py

a=int(input("Enter a Digit : "))
if a==0:
    print("{} is ZERO!!!".format(a))
elif a==1:
    print("{} is ONE".format(a))
elif a==2:
    print("{} is TWO".format(a))
elif a==3:
    print("{} is THREE".format(a))
elif a==4:
    print("{} is FOUR".format(a))
elif a==5:
    print("{} is FIVE".format(a))
elif a==6:
    print("{} is SIX".format(a))
elif a==7:
    print("{} is SEVEN".format(a))
elif a==8:
    print("{} is EIGHT".format(a))
elif a==9:
    print("{} is NINE".format(a))
elif a<0:
    print("You Entered Negative NUMBER")
else:
    print("Enter Digits Only Not NUMBER!!!")
print("Program Executed!!")

# In simple way using Dictionary
d={0:"ZERO",1:"ONE",2:"TWO",3:'THREE',4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
a=d.get(int(input("Enter Digit : ")))
if (a==None):
    print("You Entered wrong Integer, Please Enter b/w 0 to 9")
else:
    print(a)
