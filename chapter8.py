"""LOOPS"""
"""1.For Loop"""

"""range(start,stop+1,step) function"""
# range(10,101,1)  #10 to 100
# range(23,57,1)   #23 to 56
# range(57)        #0 to 56
#
# for i in range(1,10):
#     print(i)

# for i in range(6,61,6):
#     print(i)
"""take input and print table of that number"""
# n = int(input("Enter a number: "))
#
# for i in range(n,(n*10+1),n):
#     print(i)

# a = "Students"
# # for i in a:
# #     print(i)
#
# for i in range(len(a)):
#     print(f"{i}: {a[i]}")
"""Break continue and else statement"""
# for i in range(1,11):
#     # if i == 4:
#     #     break
#     # print(i)  #(1,2,3)
#     #   if i == 3 or i == 5 or i == 7:
#     #       continue
#     #   print(i)  #(1,2,4,6,8,9,10)
#       if i == 45:
#           break
#       print(i)
# else:
#     print("No break was encountered above")

"""Question Practice"""
"""1.print hello world n times"""
# n = int(input("tell your number: "))
# for i in range(1,n+1):
#     print("hello world")

"""2.print natural numbers from 1 to n"""
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i)

"""3.Reverse for loop->print n down to 1"""
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print(i)

"""4.print the multiplication table of a number"""
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{i} x {n} = {i * n}")

"""5.Sum of first n natural numbers"""
# n = int(input("till where you want to sum: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

"""6.Factorial of a number"""
# n = int(input("tell your number which you want factorial: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

"""7.print sum of all even and odd numbers in a range separately"""
# n = int(input("till where you want to sum: "))
# evensum = 0
# oddsum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         evensum += i
#
#     else:
#         oddsum += i
# print(f"sum of even numbers: {evensum}, sum of odd numbers: {oddsum}")

"""8.print all factors of a number"""
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     if n%i != 0:
#         continue
#     print(i)

"""9.check if a number is perfect"""
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         print(i)
#         sum += i
# if sum == n:
#     print("n is perfect")
# else:
#     print("n is not perfect")

"""10.check if a number is prime"""
# n = int(input("Enter a number: "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print("the number is prime")
# else:
#     print("the number is not prime")

"""11.reverse a string without using built-in functions"""
# a = input("give me a string:-")
# rev = ""
# for i in range(len(a)-1,-1,-1):
#     rev = rev+a[i]  #concatenation
# print(rev)

"""12.check if a string is a palindrome"""
# a = input("give me a string:-")
# rev = ""
# for i in range(len(a)-1,-1,-1):
#     rev = rev+a[i]  #concatenation
# if rev == a:
#     print("yes palindrome")
# else:
#     print("not palindrome")

"""13.count letters,digits and special characters in string"""
a = input("give me a string:->")
char = 0
spchar = 0
digits = 0
for i in a:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        char += 1
    elif ord(i)>=48 and ord(i)<=56:
        digits += 1
    else:
        spchar += 1
    # if i.isdigit():
    #     digits += 1
    # elif i.isalpha():
    #     char += 1
    # else:
    #     spchar += 1
print(f"letters->{char},digits->{digits},special-char->{spchar}")

