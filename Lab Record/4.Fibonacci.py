# 4. Create a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page ("/").
#     2. Accepts an integer from the URL (e.g., /7).
#     3. Generates and returns the first N Fibonacci numbers, where N is the integer passed in the URL.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Please add a number to the URL, like /5 or /10"

@app.route("/<int:number>")
def fibonacci(number):

    fibs = "First " + str(number) + " Fibonacci numbers: "

    fib1, fib2 = 0, 1

    for i in range(number):
        fibs += str(fib1) + ", "
        fib1, fib2 = fib2, fib1 + fib2

        return fibs

if __name__ == '__main__':
    app.run(debug=True)