import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friend_number = random.randint(0, len(friends))

print("Your randomly selected friend is : " + friends[random_friend_number])

print(random.choice(friends))