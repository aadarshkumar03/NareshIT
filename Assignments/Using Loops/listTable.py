'''Q26.Write a python program which will accept list of numerical integer values and display the multiplication tables for all those values. #CW
listTable.py'''

print("Enter Values seperated by comma : ")
l=[int(val) for val in input().split(",")]
for i in l:
    if i<=0:
        print("{} is Invalid Input".format(i))
        print("-"*40)
    else:
        print("\tTable for {}".format(i))
        print("-"*40)
        for j in range(1,11):
            print("\t{} x {} = {}".format(i,j,i*j))
        print("-"*40)
