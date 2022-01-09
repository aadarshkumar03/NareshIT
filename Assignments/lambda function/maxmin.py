# Q.Write an anonymous function for finding max/min value from list of numbers. #CW
# maxmin.py
maxop=lambda a:max(a)
minop=lambda a:min(a)
# main program
l=[int(val) for val in input("Enter Values Seperated By Comma : \n").split(",")]
print("{}\nMax Value={}\nMin Value={}".format(l,maxop(l),minop(l)))