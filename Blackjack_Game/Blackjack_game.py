import random
from Blackjack_art import logo


def deal_card():
    """Deals a random card from a standard deck of 52 cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if score == 21 and 11 in cards and len(cards) == 2:
        return 0
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return score
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Player's cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            game_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if game_continue == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? (yes or no): ").lower() == 'yes':
    blackjack_game()

