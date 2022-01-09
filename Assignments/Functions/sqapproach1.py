# Q.Write a python program, which will accept a numerical value and compute it's square by using functions. #HW
# sqapproach1.py

def sq(a):
    """This is a function for compute square"""
    s=a*a
    return s
# Main Program
num=int(input("Enter a number : "))
res=sq(num)
print("Square of {} = {}".format(num,res))