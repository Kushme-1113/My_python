"""while loop"""
# a = 1
# while a!=20:
#     print(a)
#     a+=1

"""Question practice"""
"""1.Seperate each digit of a number and print on a new line"""
# a = int(input("Enter the digit: "))
# while a > 0:
#     print(a%10)
#     a = a//10

"""2.Accept a number and print its reverse"""
# a = int(input("Enter the digit: "))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a%10
#     a = a//10
# print(rev)

"""3.check if a number is palindromic(equal to its reverse)"""
a = int(input("Enter the digit: "))
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a%10
    a = a//10
print(rev)
if rev == copy:
    print("The number is palindromic")
else:
    print("The number is not palindromic")


