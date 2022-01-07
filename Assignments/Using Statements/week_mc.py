# Q1.Write a python program, which will accept week number and display week name by using match...case. #CW
# using match...case statement
# week_mc.py

wkno=int(input("Enter Week Number:"))
match wkno:
	case 1:
			print("Its MONDAY")
	case 2:
			print("Its TUESDAY")
	case 3:
			print("Its WEDNESDAY")
	case 4:
			print("Its THURSDAY")
	case 5:
			print("Its FRIDAY")
	case 6:
			print("Its SATDAY")
	case 7:
			print("Its SUNDAY")
	case _:
			print("Its not a week number--learn weeks  ")
print("Program over")

# Try this one also
l1=["MONDAY","TUESDAY","WEDNESSDAY","THURSDAY","FRIDAY","MON","TUE","WED","THU","FRI"]
l2=["SATURDAY","SAT"]
l3=["SUNDAY","SUN"]
wkn=input("Enter Week Name : ")
if wkn.upper() in l1:
    print("Working Day")
elif wkn.upper() in l2:
    print("Weekend Day")
elif wkn.upper() in l3:
    print("Holiday")
else:
    print("Invalid Input....")
