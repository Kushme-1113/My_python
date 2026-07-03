"""output - print()"""
# name = "kush"
# age = 20
# print(name,age)  #basic
# print(f"my name is {name} and my age is {age}") #formatted string
# print("my name is",name, "and my age is",age) #multiple values
"""input - input()"""
# age = int(input("please enter your age:"))
# print(f"your age is {age}")

"""operators->
1.Arithmetic Operators"""
# #numbers-int,float,complex
# #(+,-,*,/,//,%,**)
# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

"""
Hierarchy of Arithmetic Operators
() -> Brackets
** -> Exponent(right to left: 2**2**3 = 2**(2**3)
* / // % -> Multiplication, division, Floor Division, Modulo
+ - -> Addition, Subtraction

"""
# #Solve
# print(3+4*2)
# print(15//4+15%4)
# print(3+2**2*5-1)

"""2.Comparison Operators"""
# print(12==12)
# print(10<20)
# print(16>29)
# print(14<=14)
# print(17>=23)
# print(19!=19)
# a = 17
# b = 46
# print(a == b)

"""3.Logical Operators"""
#and or and not

# print(12>10 and 34==34 and 45==45 and 10>20)
# print(34==45 or 12==23 or 67==69 or 12==12)
# print(not 12!=23)

"""Solve"""
# print((5>3 and 10==10) or (4!=4 and 2<1))
# print((10==10 and 23!=23) or (34==12 and bool("hello")))
# print(not(5==5 and 3!=4) or (10>20))

"""4.Assignment Operators"""
# +=,-=,*=,/=,//=,%=,**=
a = 10
a += 10
a += 10
print(a)
