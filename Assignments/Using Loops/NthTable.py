'''Q27.Write a python program which will display multiplication tables for 1 to n. #HW
NthTable.py'''

n=int(input("Enter how many tables you want : "))
if (n<=0):
    print("{} is Invalid Input".format(n))
for i in range(1,n+1):
    print("-"*30)
    print("\tTable for {}".format(i))
    print("-"*30)
    for j in range(1,11):
        print("\t{}x{}={}".format(i,j,i*j))
