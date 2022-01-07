''' Q23.Write a python program which will accept list of numerical values and sort them in both Ascending and Descending order #HW
Numsort.py'''

n=int(input("Enter How many Numbers you want in List : "))
if n<=0:
    print("Invalid Input")
else:
    l=[]
    for i in range(1,n+1):
        a=int(input("Enter {} Number : ".format(i)))
        l.append(a)
    else:
        print("Origional List={}".format(l))
        l.sort()
        print("Ascending order={}".format(l))
        l.sort(reverse=True)
        print("Descending Order={}".format(l))
