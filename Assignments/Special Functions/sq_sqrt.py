# Q.Write a python program, which will accept list of values and find their squares by using map function and also find square root list. #CW
# sq_sqrt.py
l=[int(i) for i in input("Enter Numbers Seperated by comma :\n").split(",")]
sqlst=list(map(lambda n:n**2, l))
sqrtlst=list(map(lambda n:n**0.5, l))
print("Origional List :\n%s"%l)
print("-"*40)
print("Numbers\tSquares\tSquareRoots")
print("-"*40)
for i,j,k in zip(l,sqlst, sqrtlst):
    print(" %s\t\t%s\t\t%0.2f"%(i,j,k))
print("-"*40)