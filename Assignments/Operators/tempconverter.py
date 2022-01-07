#Q3.Write a python program, which will accept temperature in celcius and convert it into fahrenheit. #HW
#tempconverter.py

c=float(input("Enter Temperature in Celcius:"))

#Formula for converting celcius into Fahrenheit and Kelvin
f= c*(9/5)+32
k= c+273.15

print("{} C(celcius) means {} F(fahrenheit) and {} K(kelvin)".format(c,f,k))
