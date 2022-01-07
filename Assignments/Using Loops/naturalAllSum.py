'''Q9.Write a python program which will calculate sum of first n natural numbers and squares and cubes of first n natural numbers. #CW
naturalAllSum.py'''

n=int(input("Enter a Number : "))
if n<=0:
    print("Invalid Number")
else:
    i=1
    s1,s2,s3=0,0,0
    while i<=n:
        print("\t{}\t{}\t{}".format(i,i**2,i**3))
        s1=s1+i
        s2=s2+i**2
        s3=s3+i**3
        i+=1
    else:
        print("\nThe sum of first {} Natural Numbers={}".format(n,s1))
        print("The sum of Square of first {} Natural Numbers={}".format(n,s2))
        print("The sum of Cubes of First {} Natural Nubers={}".format(n,s3))
print("Program Exucted!!!")
