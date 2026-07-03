"""Conditional Statements"""
# IfElse Statements : ->
# if True:
#     print(9)
# if False:
#     print(1)
# if (12==12):
#     print("12")
# if (23!=23):
#     print("hello world")

"""You have take input as age and tell the person can vote or not"""
# age = input("Enter your age: ")
# if int(age) < 18:
#     print("the person can't vote")
# else:
#     print("the person can vote")

"""Question Practice -> 1.Accept two numbers and print the greatest between them"""
# num1 = int(input("Enter the ist number: "))
# num2 = int(input("Enter the second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both the numbers are same")

"""2.Accept gender from user and print the greeting message"""
# gender = input("Please enter your gender in M or F: ")
# if gender == "M" or gender == "m":
#     print("Good Morning Sir")
# elif gender == "F" or gender == "f":
#     print("Good Morning Mam")

"""3.Accept an integer and check if it is even or odd"""
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""4.Accept a year and check if it's leap year or not"""
# year = int(input("Enter a year: "))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

"""5.Accept Temperature in degree celcious and print a description"""
# Temp = int (input ("Enter Temperature in Celcius: "))
# if Temp<0:
#     print("freezing cold")
# elif Temp>=0 and Temp<=35:
#     print("Pleasant")
# else:
#     print("Very Hot")


