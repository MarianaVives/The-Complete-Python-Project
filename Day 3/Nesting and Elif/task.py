print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age >= 18:
        print("Please pay 10 USD")
    elif 12 < age >18:
        print("Please pay 5 USD")
    elif age <= 12:
        print("Please pay 1 USD")
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
