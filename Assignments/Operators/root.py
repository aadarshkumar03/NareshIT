# Q9.Write a python program, which will calculate square root, cube root and n-th root of a given number. #HW
# root.py

# Taking Inputs
n=float(input("Enter Number:"))
r=int(input("Enter root Value:"))

# calculate n'th root
v=n**(1/r)
print("{}th root of {} = {}".format(r,n,v))
