def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

def function_1(name, surname):
    if name == "" or surname == "":
        return
    formated_f_name = name.title()
    formated_l_name = surname.title()
    return f"Your name is : {formated_f_name} {formated_l_name}"

print(function_1(input("What is you name ?"), input("What is you lastname ?")))