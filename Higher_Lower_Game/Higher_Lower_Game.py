import random, os
from Higher_lower_Game_data import data
from Higher_lower_Game_art import logo, vs


def random_word():
    """To get the random word in a random choice"""
    return random.choice(data)


def modify_word(word):
    """To modify the word in a way we could add things that are
    not in the dictionary to it, to modify it"""
    name = word['name']
    description = word['description']
    country = word['country']
    return f"{name}, a {description}, from {country}"


def compare(follower, first_word_follower, second_word_follower):
    if first_word_follower > second_word_follower:
        return follower == 'a'
    else:
        return follower == 'b'


def play_game():
    print(logo)
    game_should_continue = True
    first_word = random_word()
    second_word = random_word()
    score = 0
    while game_should_continue:
        print(f"Compare A: {modify_word(first_word)}")
        print(vs)
        print(f"Against B: {modify_word(second_word)}")
        first_word_follower = first_word['follower_count']
        second_word_follower = second_word['follower_count']
        follower = input("Who has more followers? A or B: ").lower()
        is_correct = compare(follower, first_word_follower, second_word_follower)
        os.system('cls')
        print(logo)
        if is_correct:
            score += 1
            print(f"Your current Score is {score}")
        else:
            game_should_continue = False
            print(f"you lost, your final score is {score}")
        first_word = second_word
        second_word = random_word()
        while first_word == second_word:
            second_word = random_word()
play_game()