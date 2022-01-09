# Q. Write a python Program, Which will generate first n prime Numbers. #HW
# prime1.py

def prime(n):
    if (n<=0):
        print("{} is Invalid Number".format(n))
    else:
        l=[2]
        i=2
        while len(l)<n:
            j=0
            while j<len(l):
                if (i%l[j]==0):
                    break
                elif j==len(l)-1:
                    l.append(i)
                j+=1
            i+=1
        print(l)
#main program
n=int(input("Enter How many Prime Numbers you want : "))
prime(n)

# Another Way
# def prime(n):
#     count, i = 0, 1
#     while count < n:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0: break  # Not a prime
#         else:
#             print("%d" % i, end=" ")  # print prime numbers
#             count += 1  # incrementing count
#         i += 1
#
#
# a = int(input("enter a number to print n prime numbers\t"))
# while a <= 0:
#     print("Invalid input")
#     a = int(input("enter a number to print n prime numbers\t"))
# else:
#     prime(a)