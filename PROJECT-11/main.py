import random
import os
from art import logo

deck_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def cards_for_user(list_of_cards):
  card=random.choice(list_of_cards)
  if card==11 and sum(user_cards)==20:
    card-=10
  user_cards.append(card)
  return user_cards

def cards_for_computer(list_of_cards):
  computer_cards.append(random.choice(list_of_cards))
  return computer_cards 

def finding_winner(user_result,computer_result):
    if (sum(user_result)>sum(computer_result)) and sum(user_result)<=21:
        print("You won!")
        print(f"Your cards are {user_result}")
        print(f"Computer cards are {computer_result}")
    elif sum(user_result)==sum(computer_result):
        print("It's a Draw.")
        print(f"Your cards are {user_result}")
        print(f"Computer cards are {computer_result}")
    else:
        print("You Lose.")
        print(f"Computer cards are {computer_result}")
        print(f"Your cards are {user_result}")


game_on=True
while game_on:
    print(logo)
    user_cards=[]
    computer_cards=[]
    for _ in range(2):
        result_of_user=cards_for_user(deck_of_cards)
    result_of_computer=cards_for_computer(deck_of_cards)
    print(f"Your cards are {result_of_user}\nAnd the cards for the computer are\n{result_of_computer}")
    user_choice=input("Type 'yes' if you want to pick a card again else type 'no'?\n").lower()
    if user_choice=='yes':
        result_of_user=cards_for_user(deck_of_cards)
        result_of_computer=cards_for_computer(deck_of_cards)
        finding_winner(result_of_user,result_of_computer)
    else:
        result_of_computer=cards_for_computer(deck_of_cards)
        finding_winner(result_of_user,result_of_computer)

    should_continue=input("Type 'yes' if you want to play again else type 'no'?\n").lower()
    if should_continue=='yes':
       os.system('cls')
    else:
       game_on=False
    


