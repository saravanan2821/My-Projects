while True:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))

        print("----Enter your Choice----")

        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division ")

        choice = int(input("Enter the Choice Number : "))

        match choice:
            case 1:
                print(f"{num1} + {num2} = {num1+num2}")
            case 2:
                print(f"{num1} - {num2} = {num1-num2}")
            case 3:
                print(f"{num1} * {num2} = {num1*num2}")
            case 4:
                print(f"{num1} / {num2} = {num1/num2}")
            case __:
                print("Invalid Choice")
                continue
        again = input("Do you want to continue? (yes/no)")
        if again !="yes":
          break





     #count = input("Do you wish ")



