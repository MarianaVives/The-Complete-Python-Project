import art

print(art.logo)

continue_calculating = True

def add(n1, n2):
    """Docstring: Add two numbers and returns the result (e.g. 1+2=3)"""
    return n1 + n2
def substract(n1, n2):
    """Docstring: Substract two numbers and returns the result (e.g. 2-1=1)"""
    return n1 - n2
def multiply(n1, n2):
    """Docstring: Substract two numbers and returns the result (e.g. 2*1=2)"""
    return n1 * n2
def divide(n1, n2):
    """Docstring: Substract two numbers and returns the result (e.g. 4/2=2).
    Cannot divide by zero"""
    if n2 ==0:
        print("Cannot divide by zero")
        return
    else:
        return n1 / n2
    return n1 / n2

initial_n1=True
while continue_calculating:
    if initial_n1:
        result =0
        f_number = float(input("Enter your first number: "))
    operation = input("\n+\n -\n *\n /\n Enter your operation: ")
    s_number = float(input("Enter your next number: "))

    if operation == "+":
        result= add(f_number, s_number)
        print(result)
    elif operation == "-":
        result=substract(f_number, s_number)
        print(result)
    elif operation == "*":
        result = multiply(f_number, s_number)
        print(result)
    elif operation == "/":
        result = divide(f_number, s_number)
        print(result)
    else:
        print("Invalid operation")
    continue_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation")
    if continue_result == "y":
        initial_n1 = False
        f_number=result
    else:
        initial_n1 = True




