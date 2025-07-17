# #Conditional statements
# x=10
# if x>5:
#     print("x is greater than 5")
#
# x=3
# if x>10:
#     print("x is greater than 10")
# else:
#     print("x is less than 10")
#
# x=7
# if x<5 :
#     print("x is less than 5")
# elif x==7:
#     print("x is equal to 7")
# else:
#     print("x is greater than 5")
# #loops
# for i in range(1,10):
#     print(f" i is {i}")
#
# count=1
# while count<=5:
#     print(count)
#     count+=1
#
# #loop control statements
#
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
# for i in range(3):
#     pass
# print("loop ended")
#
# #compound conditional statements
# age=30
# has_license=True
#
# if age>=18 and has_license:
#     print("you can drive")
# else:
#     print("you cannot drive")
#
# logged_in=False
# is_admin=True
#
# if logged_in or is_admin:
#     print("access granted")
# else:
#     print("access denied")
#
# #FizzBuzz problem
#
# for i in range(1,51):
#     if i % 3 == 0 and i % 5==0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
# #fIZZBUZZ PROBLEM WITH USER INPUT
#
# start=int(input("enter any starting number:"))
# end=int(input("enter any ending number:"))
# for i in range(start,end+1):
#     if i % 3 == 0 and i % 5==0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
# numbers=list(map(int,input("enter a list of numbers separated by space").split()))
# for num in numbers:
#       square=num **  2
#       print(square)

#checking prime numbers in a range
#
# start= int(input("enter start number"))
# end=int(input("enter end number"))
#
# print(f"generating range between {start} and {end} number:")
# print("prime numbers in given range are:")
#
# for i in range(start,end+1):
#
#     if i < 2:
#         continue
#     is_prime=True
#     for num in range(2,int(i**0.5)+1):
#         if i % num == 0:
#             is_prime=False
#             break
#
#     if is_prime:
#         print(i)
#

# RIGHT ANGLED TRIANGLE:

# n=int(input("enter any number"))
#
# for i in range (n):
#     for j in range(i):
#         print('*',end=" ")
#     print()

n=int(input("enter any number"))
for i in range(n):
    for j in range(i):
        print("  *  " , end=" ")
    print()








