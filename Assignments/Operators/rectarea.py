#Q4.Write a python program, which will accept length and breadth of rectangle and find it's area and circumerence. #CW
#rectarea.py

l=float(input("Enter Length:"))
b=float(input("Enter Breadth:"))

#calulate area and perimeter / circumference
ar=l*b
pr=2*(l+b)

# diplay the result
print("-"*50)
print("Length={}".format(l))
print("Breadth={}".format(b))
print("Area of Rect={}".format(ar))
print("Peri of Rect={}".format(pr))
print("-"*50)
