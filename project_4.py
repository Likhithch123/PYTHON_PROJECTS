## Title of the project: ROCK, PAPER, SCISSORS GAME.

import random
print("Welcome! to the game of ROCK, PAPER, SCISSORS.")
users_choice=input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")
game_list=['0','1','2']
computers_choice_int=random.randint(0,len(game_list)-1)
computers_choice=game_list[computers_choice_int]

game_pillars=['Rock','Paper','Scissors']

rock_ascii_art='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper_ascii_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_ascii_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ascii_art_list=[rock_ascii_art,paper_ascii_art,scissors_ascii_art]

if int(users_choice)>=0 and int(users_choice)<3:
    print(f"ASCII art of {game_pillars[int(users_choice)]}")
    print(ascii_art_list[int(users_choice)])
    print("\nComputer chose:\n")
    print(computers_choice)
    print(f"ASCII art of {game_pillars[int(computers_choice)]}")
    print(ascii_art_list[int(computers_choice)])
if users_choice==computers_choice:
    print("Draw! you both chose the same.\n")
elif users_choice=='0':
    if computers_choice=='1':
        print("\nYou Lose!")

    else:
        print("\nYou Won!")
elif users_choice=='1':
    if computers_choice=='0':
        print("\nYou Won!")

    else:
        print("\nYou Lose!")
elif users_choice=='2':
    if computers_choice=='0':
        print("\nYou Lose!")

    else:
        print("\nYou Won!")

else:
    print("You lose, Invalid choice.")
print("\nThanks for playing.\nGAME OVER.")