import random
import art

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
p_cards_list =[]
d_cards_list =[]
dealer_score = -1
player_score = -1

wants_to_play = True

def begin_game():
    """Print art and ask if ready to begin"""
    print(art.logo)
    p_cards_list.clear()
    d_cards_list.clear()

def deal_a_card():
    card = random.choice(deck)
    return card

def deal_initial_cards():
    """Deal cards for the player and dealer (computer) and add them to their respective lists/decks"""

def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards)== 21 and len(cards)==2:
        return 0
    #Soft 7
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, d_score):
    if p_score == d_score:
        return "Tie"
    elif d_score ==0:
        return "Dealer has a blackjack! You lose."
    elif p_score ==0:
        return "Player has a blackjack! You win!"
    elif p_score > 21:
        return "You went over. You lose!"
    elif d_score > 21:
        return "Dealer went over. You win!"
    elif p_score > d_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    is_game_over = False

    for _ in range(2):
        p_cards_list.append(deal_a_card())
        d_cards_list.append(deal_a_card())

    while not is_game_over:
        player_score = calculate_score(p_cards_list)
        dealer_score = calculate_score(d_cards_list)
        print(f"Your cards : {p_cards_list} and your current score : {player_score}")
        print(f"Dealer first card is : {d_cards_list[0]}")

        if player_score ==0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            deal_another_card = input("Do you want to deal again? (y/n): ")
            if deal_another_card == "y":
                card = deal_a_card()
                p_cards_list.append(card)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        print("Let's deal another card for the dealer")
        card = deal_a_card()
        d_cards_list.append(card)
        print("Dealer new card is: " + str(card))
        dealer_score = calculate_score(d_cards_list)

    print(f"Your final hand is: {p_cards_list} and your score is {player_score}")
    print(f"Dealer's hand is: {d_cards_list} and its score is {dealer_score}")
    print(compare(player_score, dealer_score))

while wants_to_play:
    begin_game()
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "n":
        wants_to_play = False
    else:
        wants_to_play = True



