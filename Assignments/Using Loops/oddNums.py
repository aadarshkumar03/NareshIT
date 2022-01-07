'''Q3.Write a python program, which will generate odd numbers within n . #HW
oddNums.py
'''

n=int(input("Enter Number : "))
if n<=0:
	print("Invalid Number")
else:
	i=1
	while i<=n:
		print(i)
		i=i+2
