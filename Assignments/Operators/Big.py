# Q12.Write a python program, which will accept two numerical values and decide the biggest among them. #HW
# Big.py

a=int(input("Enter Value of a:"))  
b=int(input("Enter Value of b:")) 
big=a  if(a>b)   else  b    # This "if....else  is called Ternary Operator.
print("Big({},{})={}".format(a,b,big))
