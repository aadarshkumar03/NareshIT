# Q.Write a python program, which will accept list of values and find list of positive, negative elements by using filter funciton. #HW
#  posneg.py
l=[int(i) for i in input("Enter Numbers Seperated by comma :\n").split(",")]
zerolst=list(filter(lambda n:n==0, l))
poslst=list(filter(lambda n:n>0, l))
neglst=list(filter(lambda n:n<0, l))
print("Origional List :\n%s"%l)
print("Zero Numbers List : \n%s"%zerolst)
print("Positive Numbers  List :\n%s"%poslst)
print("Negative Numbers List :\n%s"%neglst)