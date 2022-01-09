# Q.Write an anonymous function for finding the biggest among three numbers. #HW
# big2.py
bigop=lambda a,b,c : "EQUAL" if (a==b==c) else a if (a>b) and (a>c) else b if (b>a) and (b>c) else c
#main program
n1,n2,n3=int(input("Enter First Number : ")), int(input("Enter Second Number : ")), int(input("Enter Third Number : "))
print("BIG({},{},{})={}".format(n1,n2,n3,bigop(n1,n2,n3)))