# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

name= input("Your Name: ")
age= input("Your Age: ")
city= input("Your City: ")
def greet_input(name, age):
    print(f"Hello {name}, you are {age} years old, you live in {city}")

greet_input(name, age)