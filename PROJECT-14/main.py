import art 
from random import choice
from game_data import data
from os import system

print(art.logo)
user_score=0

def verifying_guess(data1,data2):
  if data1['follower_count'] > data2['follower_count']:
    return 'A'
  else:
    return 'B'

rand_data1=choice(data)
rand_data2=choice(data)
guess=True
while guess:
  print(f"Compare A: {rand_data1['name']}, a {rand_data1['description']}, from {rand_data1['country']}.")
  print(art.vs)
  print(f"Against B: {rand_data2['name']}, a {rand_data2['description']}, from {rand_data2['country']}.")
  user_guess=input("Who has more followers? Type 'A' or 'B':\n").upper()
  result=verifying_guess(rand_data1,rand_data2)
  if user_guess==result:
    user_score+=1
    system('cls')
    print(art.logo)
    print(f"You are right! Current score: {user_score}.")
  else:
    guess=False
    system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {user_score}.")
  rand_data1=rand_data2
  rand_data2=choice(data)
  if rand_data1['name']==rand_data2['name']:
    rand_data2=choice(data)
  