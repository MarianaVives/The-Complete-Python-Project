print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
wants_pepperoni = 3
wants_extra_cheese  = 1

total = 0

#Pick a size
if size == "S":
   total= small_pizza
elif size == "M":
    total = medium_pizza
else:
    total = large_pizza

#Pepperoni
if pepperoni == "Y":
    total+= wants_pepperoni
else: total

#Extra cheese
if extra_cheese == "Y":
    total+= wants_extra_cheese;
else: total

print(f"Your final bill is: ${total}.")