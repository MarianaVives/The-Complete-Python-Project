import random
import art


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
lives=0

def random_1_to_100():
    """Return a random integer in the range 1..100 (inclusive)."""
    return random.randint(1, 100)

def print_intro():
    """Print the intro message."""
    print(art.logo)
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

def print_winner(ans):
    """Print the winner message."""
    print(f"You win! The answer was {ans}")

def print_too_low():
    """Print the too low message."""
    print("Your guess is too low.")

def print_too_high():
    """Print the too high message."""
    print("Your guess is too high.")

def ask_difficulty():
    """Print the difficulty message."""
    print("You have 10 attempts if you choose easy. You have 5 attempts if you choose difficult.")
    difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")
    if difficulty == "e":
        return EASY_LEVEL_TURNS
    elif difficulty == "h":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input")
        return None

def print_lives(no_lives):
    """Print the number of lives."""
    print(f"You have {no_lives} lives.")

def ask_for_number():
    """Ask the user to enter a number."""
    guess = input("Make a guess: ")
    return guess

def count_lives(lr):
    """Count the number of lives."""
    return lr - 1

def compare_guess(no_lives, p_guess, no_to_guess):
    """Compare the guess vs the correct number. It returns number of lives remaining"""
    if p_guess > no_to_guess:
        print_too_high()
        return no_lives-1
    elif p_guess < no_to_guess:
        print_too_low()
        return no_lives-1
    else:
        print_winner(no_to_guess)
        print(art.win)

def ask_repeat():
    repeat_game = input("Do you want to play again? y/n ")
    # Ask if wants to play again
    if repeat_game == "n":
        game_over = True
    return game_over

def game():
    game_over = False
    while not game_over:
        #Start Game
        print_intro()
        #Generate number to guess from 1 to 100
        num_to_guess = random_1_to_100()
        #Ask difficulty
        lives = ask_difficulty()
        #Compare the ans with the gues
        guess = 0
        while num_to_guess != guess:
            print_lives(lives)
            guess = int(ask_for_number())
            lives = compare_guess(lives, guess, num_to_guess)
            if lives ==0:
                return
            elif guess != num_to_guess:
                print("Guess again.")
game()