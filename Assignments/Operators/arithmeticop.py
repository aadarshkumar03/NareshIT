#Q7.Write a python program, which will accept two numerical values and perform different types of arithmetic operations.#CW
#arithmeticop.py

#Taking Inputs
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))

#Displaying Results
print("-"*40)
print("Arithmetic Operations")
print("-"*40)
print("Sum({},{})={}".format(a,b,a+b))
print("Sub({},{})={}".format(a,b,a-b))
print("Mul({},{})={}".format(a,b,a*b))
print("Div({},{})={}".format(a,b,a/b))
print("Floor div({},{})={}".format(a,b,a//b))
print("Mod({},{})={}".format(a,b,a%b))
print("Expo({},{})={}".format(a,b,a**b))
print("-"*40)
