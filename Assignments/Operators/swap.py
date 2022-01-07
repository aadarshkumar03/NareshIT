# Q10.Write a python program, which will accept any type of two values and swap them. #CW
# swap.py

#Taking Inputs
a=input("Enter Value a:")
b=input("Enter Value b:")

# Display Results
print("="*40)
print("Orginal Val of a={}".format(a))
print("Orginal Val of b={}".format(b))
print("="*40)

#swaping logic
a,b=b,a
print("Swapped Val of a={}".format(a))
print("Swapped Val of b={}".format(b))
print("="*40)
