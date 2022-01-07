#Q5.Write a python program, which will accept radius of circle and find it's area and perimeter. #HW
#circlearea.py 

r=float(input("Enter Radius of Circle:"))

#Calculating Area and Perimeter of Circle
pi=3.14
a=pi*(r**2)
p=2*pi*r

#Display Results
print("Radius of Circle = {}".format(r))
print("Perimeter of Circle = {}".format(p))
print("Area of Circle = {}".format(a))
