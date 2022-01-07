# Q11.Write a python program, which will demostrate the functionality of relational operators. #CW
# relationalop.py

# Taking Inputs
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))

# Display Results
print("*"*50)
print("\tRelational Operations")
print("*"*50)
print("\t{}>{}={}".format(a,b,a>b))
print("\t{}>{}={}".format(b,a,b>a))
print("\t{}<{}={}".format(a,b,a<b))
print("\t{}<{}={}".format(b,a,b<a))
print("\t{}=={}={}".format(a,b,a==b))
print("\t{}!={}={}".format(a,b,a!=b))
print("\t{}>={}={}".format(a,b,a>=b))
print("\t{}<={}={}".format(a,b,a<=b))
print("*"*50)
