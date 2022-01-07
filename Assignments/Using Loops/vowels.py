'''Q21.Write a python program which will accept a line of text and print vowels. #HW
vowels.py'''

s=input('Enter a String/Line : ')
l=['a','e','i','o','u']
for i in range(len(s)):
    for j in l:
        if s[i] in j:
            print(s[i],end=",")
print()
#another way to find vowels
s=input("Enter a String/Line: ")
l=['aeiou']
for v in s:
    if v in l[0]:
        print(v,end=",")
