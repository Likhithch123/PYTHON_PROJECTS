import random
import hangman_words
import hangman_art

print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
# print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
lives = 7
user_chosen_chars = []
end_of_game = False
while not end_of_game:
    guess = input("Guess any character:").lower()
    if guess in user_chosen_chars:
        print(f"You have already chosen {guess}.\n{user_chosen_chars}")
        continue
    else:
        user_chosen_chars.append(guess)
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The chosen word is {chosen_word}.")
