import random

from flask import Flask

app = Flask(__name__)


def add_html_tag(*args):
    def wrapper(function):
        return f"<{args[0]}>{function()}<{args[0]}/>"

    return wrapper


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/qq7ef70oHLoAM" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/qq7ef70oHLoAM">via GIPHY</a></p>'


def too_low():
    return "<h1 style='color:teal'>Too Low</h1>" \
           "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"


def too_high():
    return "<h1 style='color:red'>Too High</h1>" \
           "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"


def correct():
    return "<h1 style='color:lime'>Correct answer</h1>" \
           "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


n = random.randint(0, 9)


@app.route("/<int:number>")
def game(number):
    if n == number:
        return correct()
    elif n < number:
        return too_high()
    else:
        return too_low()


if __name__ == "__main__":
    app.run(debug=True)
