'''Q22.Write a python program which will accept list of values and find there sum and average. #CW
listSumAvg.py'''

n=int(input("How many numbers you want in List : "))
if n<=0:
    print("Invalid Input")
else:
    l=[]
    s=0
    for i in range(1,n+1):
        a=int(input("Enter {} Number  : ".format(i)))
        l.append(a)
    else:
        for j in range(0,len(l)):
            s=s+l[j]
        else:
            print("Sum={}".format(s))
            print("Average={}".format(s/len(l)))
