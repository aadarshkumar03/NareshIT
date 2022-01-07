'''Q24.Write a python program which will accept list of student names and sort them in alphabetical order Both Ascending and Descending. #HW
Namesort.py'''

n=int(input("How many names you want to enter : "))
if n<=0:
    print("Invalid Input")
else:
    l=[]
    for i in range(1,n+1):
        a=input("Enter {} Name : ".format(i))
        l.append(a.capitalize()) #Here capitalize function
    else:
        print("Origional List={}".format(l))
        l.sort()
        print("Names in ASCending Order={}".format(l))
        l.sort(reverse=True)
        print("Names in DEScending Order={}".format(l))
