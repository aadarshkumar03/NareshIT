'''Q25.Write a python program which will accept list of values. and accept a value and search in list of values and find whether it is present or not. #HW
Numsearch.py'''

n=int(input("Enter how many values you want in List : "))
if n<=0:
    print("Invalid Input")
else:
    l=[]
    for i in range(1,n+1):
        a=int(input("Enter {} Number : ".format(i)))
        l.append(a)
    else:
        print("Origional List={}".format(l))
        b=int(input("Enter which value you want to search:"))
        if b in l:
            print("The value {} is in list for {} time".format(b,l.count(b)))
        else:
            print(b, "is not in List")
