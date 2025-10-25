# 5. Create a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page (/).
#     2. Accepts an integer from the URL (e.g., /6).
#     3. Calculates the factorial of the given number and displays the result in the browser.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Please add a number to the URL, like /5 or /10"

@app.route("/<int:number>")
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i

        return f"Factorial of {number} is: {fact}"

if __name__ == '__main__':
    app.run(debug=True)