''' Q1.Write a python program which will generate 1 to n numbers, where n must be the positive integer value #CW
generateNum.py
'''

n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	i=1           # initlizatioon part
	while(i<=n):  # condition part
		print("val of i={}".format(i))
		i=i+1       # updation part
