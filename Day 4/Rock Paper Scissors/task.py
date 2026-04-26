import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option = input("What do you choose? Rock (0), Paper (1), Scissors(2)")

if option == "0":
    option = rock
elif option == "1":
    option = paper
elif option == "2":
    option = scissors
else:
    print("Invalid option")

print("You choose : " + option)

computer_list = [rock, paper, scissors]

computer = random.choice(computer_list)
print("Computer chose : " + computer)

if computer == option:
    print("You draw")
elif computer == scissors:
    if option == rock:
        print("You win")
    else:
        print("You lose")
elif computer == rock:
    if option == paper:
        print("You win")
    else:
        print("You lose")
elif computer == paper:
    if option == scissors:
        print("You win")
    else:
        print("You lose")
