def my_function():
    result = 3*2
    return result

print(my_function())

def format_name(f_name, l_name):
    new_name = f_name.title()
    new_lname = l_name.capitalize()
    return f"{new_name} {new_lname}"

print(format_name("mArIana", "ISLAS"))