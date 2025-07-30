"""num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 >=0 and num2>=0:
    print(num1 +num2)
else:
    print("Please enter positive number")"""
from ctypes import HRESULT

"""

year = int(input("Enter a Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
"""

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))

print("Please Enter your choice")
print("1. Addition")
print("2. Substraction")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice"))

if choice==1:
    result= num1 + num2
    print("Result",result)
elif choice==2:
    result= num1 - num2
    print("Result",result)
elif choice==3:
    result= num1 * num2
    print("Result",result)
elif choice==4:
    result= num1 / num2
    print("Result",result)
else:
    print("invalid Choice")


"""a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))

print("1.Addition\n2.Substraction\n3.Multiply\n4.Divide")
choice =int(input("Enter your choice : "))
match choice:
    case 1:
        print(f"{a} + {b} = {a+b}")
    case 2:
        print(f"{a} - {b} = {a-b}")
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case __:
        print("invalid choice")"""

