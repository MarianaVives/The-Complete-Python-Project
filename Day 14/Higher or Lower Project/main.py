import game_data
import random
import art

data_for_comparison = game_data.data

def game():
    first_element_to_compare = ""
    second_element_to_compare = ""
    game_over = False
    round_number = 0
    while not game_over:
        print(art.logo)
        if round_number == 0:
            for _ in range(1):
                #Select a random item from list to begin with and bring the object
                first_element_to_compare = data_for_comparison[random.randint(0, len(data_for_comparison) - 1)]
                second_element_to_compare = data_for_comparison[random.randint(0, len(data_for_comparison) - 1)]
                if first_element_to_compare == second_element_to_compare:
                    second_element_to_compare = data_for_comparison[random.randint(0, len(data_for_comparison) - 1)]
        elif round_number >= 1:
            first_element_to_compare = second_element_to_compare
            second_element_to_compare = data_for_comparison[random.randint(0, len(data_for_comparison) - 1)]
            if first_element_to_compare == second_element_to_compare:
                second_element_to_compare = data_for_comparison[random.randint(0, len(data_for_comparison) - 1)]

        #Iterate through object to bring name and followers from object a and object b
        name_a = first_element_to_compare["name"]
        count_a = first_element_to_compare["follower_count"]
        description_a = first_element_to_compare["description"]
        country_a = first_element_to_compare["country"]
        name_b = second_element_to_compare["name"]
        count_b = second_element_to_compare["follower_count"]
        description_b = second_element_to_compare["description"]
        country_b = second_element_to_compare["country"]


        #Display options
        print(f"Compare Option A : {name_a}, {description_a}, from {country_a}")
        print(art.vs)
        print(f"Against Option B : {name_b}, {description_b}, from {country_b}")

        #Ask user to vote between item A vs B
        guess = input("Who has more followers ? A/B").lower()
        guess_object=[]
        if guess == "a":
            guess_object = first_element_to_compare
        else:
            guess_object = second_element_to_compare
        #compare Values and choose highest
        high = max(count_a, count_b)
        higher_list = []

        if high == count_a:
            higher_list.append(name_a)
        elif high == count_b:
            higher_list.append(name_b)

        if guess_object["name"] in higher_list:
            round_number += 1
            print(f"you are correct! Your current score is: {round_number}")
        else:
            print(f"Sorry that is wrong. Your score is : {round_number}")
            game_over = True

game()