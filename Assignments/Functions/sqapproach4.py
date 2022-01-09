#function for calculate square by using function(approch-4)
#sqapproach4.py
def sq():
    a=int(input("Enter a Number : "))
    s=a*a
    return a,s
a,res=sq()
print("Square of {} = {}".format(a,res))
print("-"*50)
print("\tUsing Single variable as <class, 'tuple'>")
print("-"*50)
res=sq()
print("Square of {} = {}".format(res[0],res[1]))