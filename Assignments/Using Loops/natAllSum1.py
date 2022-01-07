'''Q14.Write a python program which will calculate sum of n natural numbers, squares and cubes of n natural numbers. #HW
natAllSum1.py'''

n=int(input("Enter a Number : "))
s1,s2,s3=0,0,0
for i in range(1,n+1):
    print("\t{}\t{}\t{}".format(i,i**2,i**3))
    s1=s1+i
    s2=s2+i**2
    s3=s3+i**3
else:
    print("-"*50)
    print("\t{}\t{}\t{}".format(s1,s2,s3))
    print("-"*50)
    print("The sum of First {} Numbers = {}".format(n,s1))
    print("The sum of Squares of First {} Natural Numbers = {}".format(n,s2))
    print("The sum of Cubes of First {} Natural Numbers = {}".format(n,s3))
print("Program Executed!!!")
