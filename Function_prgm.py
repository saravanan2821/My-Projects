"""def Greeting(name,age):
    print("Hi",name,"You are",age,"years old")

Greeting("Saravanan",24)
Greeting(age=24,name="Saravanan")

def is_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is Odd")

number = int(input("Enter the number : "))
is_even(number)"""


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"factorial of {num} is {fact}")

num = int(input("Enter the number : "))
factorial(num)





