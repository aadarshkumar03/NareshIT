# Q.Write a python program, which will retrieve all values from a given line of text and print the numbers of vowels and consonants. #CW
# vow_cons.py
s=input("Enter String / Line of text :\n")
vowlst=list(filter(lambda n:n.lower() in ('a','e','i','o','u'),s))
conslst=list(filter(lambda n:n.lower() not in ('a','e','i','o','u'),s))
print("Origional String is %s"%s)
print("Vowels in Given String : %s"%vowlst)
print("Consoonents in Given String : %s"%conslst)
print("Number of Vowels used in string is %d"%len(vowlst))
print("Number of Consonants used in string is %d"%len(conslst))