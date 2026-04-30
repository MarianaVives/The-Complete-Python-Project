# Modifying Global Scope

enemies = 1

"""def increase_enemies():
    global enemies #Changes the value of the whole function
    enemies += 1
    print(f"enemies inside function: {enemies}")
"""
def increase_enemies_2():
    print(f"enemies inside function: {enemies}")
    return enemies + 3

#increase_enemies()
#print(f"enemies outside function: {enemies}")
enemies = increase_enemies_2()
print(f"enemies outside function 2: {enemies}")

