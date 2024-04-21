from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    global flip_timer, current_card
    current_card = choice(data_dict)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def is_known():
    global current_card
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv('../python-projects/PROJECT-31/data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="../python-projects/PROJECT-31/images/card_front.png")
card_back_image = PhotoImage(file='../python-projects/PROJECT-31/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

try:
    data = pandas.read_csv("../python-projects/PROJECT-31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv('../python-projects/PROJECT-31/data/french_words.csv')
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')


current_card = choice(data_dict)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='../python-projects/PROJECT-31/images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='../python-projects/PROJECT-31/images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
