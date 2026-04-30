enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_juice():
    juice_sweetness = 5
    print(juice_sweetness)


drink_juice()