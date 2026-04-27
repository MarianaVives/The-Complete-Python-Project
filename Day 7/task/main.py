import random
from hangman_words import word_list as wl
from hangman_art import stages as s
from hangman_art import logo as l

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(wl)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
incorrect_letters = []
lives = 6

print(l)
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You have already guessed this letter : " + guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    if guess not in chosen_word:
        if guess in incorrect_letters:
            print("You have already guessed this letter : " + guess)
        else:
            incorrect_letters.append(guess)
            lives -= 1
            print(s[lives])
        print("Incorrect guesses : " + str(incorrect_letters))

        if lives == 0:
            game_over = True
            print("you lose")

    print(display)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
