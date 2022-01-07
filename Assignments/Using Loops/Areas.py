'''Q30.Write a python program which will implement the following menu driven application.
    Area of different figures :
    i)Rectangle ii)Square iii)Circle iv)Triangle v)Exit #CW
Areas.py'''

import sys,math
while(True):
	print("-"*50)
	print("\tArea of Different Figures")
	print("-"*50)
	print("\t1.Rectangle")
	print("\t2.Square")
	print("\t3.Circle")
	print("\t4.Trinagle")
	print("\t5.Exit")
	print("-"*50)
	ch=int(input("Enter Ur Choice:"))
	match ch:
		case 1:
			l=float(input("Enter Length:"))
			b=float(input("Enter Breadth:"))
			ra=l*b
			print("Area of Rectangle={}".format(ra))
		case 2: 
			s=float(input("Enter Side:"))
			sa=s**2
			print("Area of Square={}".format(sa))
		case 3:
			r=float(input("Enter Radius:"))
			ca=math.pi*r**2
			print("Area of Circle={}".format(ca))
		case 4:
			a=float(input("Enter Value of a :"))
			b=float(input("Enter Value of b:"))
			c=float(input("Enter Value of c:"))
			s=(a+b+c)/2
			at=(s*(s-a)*(s-b)*(s-c))**0.5
			print("Area of Triangle={}".format(at))
		case 5:
					print("Thx for using this Program!")
					sys.exit()
		case _: 
				print("Ur choice operation is wrong--try again")
