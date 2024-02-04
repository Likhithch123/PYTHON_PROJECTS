from art import logo
from random import randint
from os import system


def evaluating(no_of_turns):
    flag = False
    print(
        f"You have a total of {no_of_turns} attempts for guessing the number.")
    while no_of_turns > 0 and not flag:
        user_guess = int(input("Guess a number?\n"))
        if user_guess == computers_choice:
            print(f"You got it! The number is {computers_choice}.")
            flag = True
        elif computers_choice > user_guess:
            no_of_turns -= 1
            print(f"Too low. Guess again. You have {no_of_turns} left.")
        elif computers_choice < user_guess:
            no_of_turns -= 1
            print(f"Too high. Guess again. You have {no_of_turns} left.")
        else:
            pass
    if flag == False:
        print(
            f"You lose. You run out of turns. The number is {computers_choice}."
        )


game_on = True
while game_on:
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    computers_choice = randint(1, 100)
    difficulty_level = input(
        "Enter your preffered level of game 'easy' or 'hard'?\n").lower()
    if difficulty_level == 'easy':
        evaluating(10)
    elif difficulty_level == 'hard':
        evaluating(5)
    else:
        print("Invalid difficulty level.")
    users_choice = input(
        "Type 'yes' if you want to play again else type 'no'\n").lower()
    if users_choice == 'yes':
        system('cls')
    else:
        game_on = False
