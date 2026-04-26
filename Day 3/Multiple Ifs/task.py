print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickers are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_foto = input("Do you want a photo taken y/n");
    if wants_foto == "y":
        print("Each photo is 3 USD")
        #bill = bill + 3
        bill+=3
    else:
        print("You can't take a photo")
    print(f"Total is : {bill} USD")
else:
    print("Sorry you have to grow taller before you can ride.")
