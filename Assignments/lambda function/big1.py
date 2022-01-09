# Q.Write a pytohn program, which will find biggest among two numbers. #CW
# big1.py
bigop=lambda a,b:"EQUAL" if a==b else a if a>b else b
#main program
n1,n2=int(input("Enter value of a : ")), int(input("Enter value of b : "))
print("Big({},{})={}".format(n1,n2,bigop(n1,n2)))