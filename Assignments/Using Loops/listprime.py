'''Q28.Write a python program which will accept list of values and decide which are prime or not. #CW
listprime.py'''

print("Enter values seperated by comma : ")
l=[int(val) for val in input().split(",")]
for i in l:
    if i<=1:
        print("{} is Invalid Input".format(i))
    else:
        res=True
        for j in range(2,i):
            if i%j==0:
                res=False
                break
        if res:
            print("{} is Prime Number".format(i))
        else:
            print("{} is not Prime".format(i))
