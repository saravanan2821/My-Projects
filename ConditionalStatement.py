age = int(input("Enter your Age:"))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a Senior citizen.")
