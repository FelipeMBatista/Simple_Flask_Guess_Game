import random
from flask import Flask

app = Flask(__name__)
random_generate = random.randint(a=0, b=9)

gifs = [
    'https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif',
    'https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif',
    'https://media.giphy.com/media/7SF5scGB2AFrgsXP63/giphy.gif',
    'https://media.giphy.com/media/T1WqKkLY753dZghbu6/giphy.gif',
    'https://media.giphy.com/media/Ty9Sg8oHghPWg/giphy.gif',
    'https://media.giphy.com/media/cr9vIO7NsP5cY/giphy.gif',
    'https://media.giphy.com/media/KbZEMiWBFdynuQUobJ/giphy.gif',
    'https://media.giphy.com/media/TGMBfijgHh5FzsR1fT/giphy.gif',
    'https://media.giphy.com/media/ZeFHQos2dpaYTtNcQJ/giphy.gif'
]

righ_gifs = [
    'https://media.giphy.com/media/LRNxdA0soqs09YWa4F/giphy.gif',
    'https://media.giphy.com/media/3og0ILzGlzG26yNINq/giphy.gif',
    'https://media.giphy.com/media/wkahtbq3roKK94GK6A/giphy.gif',
    'https://media.giphy.com/media/U3I5ZJPFJpXRm/giphy.gif',
    'https://media.giphy.com/media/fa4E839VTHoFJZ02Mo/giphy.gif',
    'https://media.giphy.com/media/UAXK9VGoJTbdcPgmcJ/giphy.gif',
    'https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif'
]

def check_answer(function):
    def wrapper(num):
        global random_generate
        if num > 9:
            return '<h1>Guess a number between 0 and 9</h1>' \
                   '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        elif num < random_generate:
            return f'<h1 style="color: red;">Too low. Try again!</h1>' \
                   f'<img src={random.choice(gifs)}>'
        elif num > random_generate:
            return f'<h1 style="color: red;">Too High. Try again!</h1>' \
                   f'<img src={random.choice(gifs)}>'
        elif num == random_generate:
            return f'<h1 style="color: green;">You got it!</h1>' \
                   f'<img src={random.choice(righ_gifs)}>'
    return wrapper

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
@check_answer
def show_result(num):
    return None

if __name__ == "__main__":
    app.run(debug=True)