#Q6.Write a python program, which will calculate area and circumference of square by accepting value of side. #HW
#sqarea.py

s=float(input("Enter value of side of Square:"))

#Calculating Area and Circumference of Square
a=s**2
c=4*s

#Display Results
print("Length of Square is {}".format(s))
print("Area of Square is {}".format(a))
print("Circumference of Square is {}".format(c))
