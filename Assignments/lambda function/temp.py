# Q.Write a python program which will accept list of temperature in celcius and calculate there equvalant fahrenheit
# temperature. #CW
# #temp.py
temp=lambda a:(a*9/5)+32

# main program
l=[int(val) for val in input("Enter values Seperated By Comma :\n").split(",")]
for i in l:
    print("({})C--->({})F".format(i,temp(i)))


# (OR)
# l=[int(val) for val in input("Enter values Seperated By Comma :\n").split(",")]
# print("List of Temperature in Celcius : \n{}".format(l))
# f=[(i*9/5)+32 for i in l]
# print(f)