'''Q18.Write a python program which will accept age of citizen and decide eligible for vote or not. #CW
VoteExample.py'''

while(True):
	age=int(input("Enter the age of Citizen"))
	if((age>=18) and (age<=100) ):
		break
print("Citizen is eligible to Vote")
