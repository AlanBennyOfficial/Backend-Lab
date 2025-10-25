# 3. Write a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page ("/").
#     2. Accepts an integer from the URL (e.g., /10).
#     3. Generates and returns all prime numbers up to the given integer as a string.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Please add a number to the URL, like /5 or /10"

@app.route("/<int:number>")
def prime(number):
    primes = "" 
    for i in range(2, number + 1):

        for n in range(2, (i // 2) + 1):
            if i % n == 0:
                break
            else:
                primes += str(i) + ", "
    return primes

if __name__ == '__main__':
    app.run(debug=True)