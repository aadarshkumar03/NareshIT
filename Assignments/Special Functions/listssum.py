# Q.Write a python program, which will compute sum of contents of two lists by using map function. #CW
# listssum.py
l1=[int(i) for i in input("Enter Values seperated by comma :\n").split(",")]
l2=[int(i) for i in input("Enter Values Seperated by Comma :\n").split(",")]
listsum=list(map(lambda x,y:x+y, l1,l2))
print("Sum of Two List ",listsum)
print("----------------OR---------------------")
print("List1\tList2\tSum")
for i,j in zip(l1,l2):
    print("{}\t+\t{} = \t{}".format(i,j,i+j))