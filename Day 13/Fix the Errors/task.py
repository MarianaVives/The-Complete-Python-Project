try:
    age = int(input("How old are you?"))
except ValueError:
    print("Enter a valid number e.g. 18.")
    age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You cannot drive at age {age}.")