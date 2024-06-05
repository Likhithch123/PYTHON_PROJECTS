from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def home_route():
    return '<h1>Guess a number between 0 and 9\n<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:user_choice>')
def check_result(user_choice):
    if user_choice > random_num:
        return '<h1 style="color: Red">Too High, Try Again\n<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    
    elif user_choice < random_num:
        return '<h1 style="color: Purple">Too Low, Try Again\n<img src=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return '<h1 style="color: Green">You Found Me!</h1>\n<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

random_num = randint(0, 9)

if __name__ == '__main__':
    app.run(debug=True)