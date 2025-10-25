Sure! Here's the corrected and properly formatted Python Flask code with the questions commented out:

```python
# 1. Create a simple view that returns "Hello, World!" and map it to a URL using Python Flask.
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello():
    return "Hello, World!"

# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# 2. Create a Flask view that displays a list of hyperlinks to various social media websites using a Jinja template, and map it to a URL route.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/social')
def social_links():
    # List of social media sites
    links = {
        "Facebook": "https://www.facebook.com",
        "Twitter": "https://www.twitter.com",
        "Instagram": "https://www.instagram.com",
        "LinkedIn": "https://www.linkedin.com",
        "YouTube": "https://www.youtube.com"
    }
    return render_template("social.html", links=links)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/social.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Social Media Links</title>
</head>
<body>
    <h2>Social Media Links</h2>
    <ul>
        {% for name, url in links.items() %}
        <li><a href="{{ url }}" target="_blank">{{ name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```python
# 3. Write a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page ("/").
#     2. Accepts an integer from the URL (e.g., /10).
#     3. Generates and returns all prime numbers up to the given integer as a string.

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    # Message asking user to enter a number in the URL
    return "Please add a number to the URL, like /5 or /10"

# Route that accepts an integer from the URL
@app.route("/<int:number>")
def prime(number):
    primes = ""  # String to hold prime numbers
    # Loop through all numbers from 2 to 'number'
    for i in range(2, number + 1):
        # Check if 'i' is prime
        for n in range(2, (i // 2) + 1):
            if i % n == 0:  # If divisible, not a prime
                break
        else:
            # If no divisor found, it is prime → add to result string
            primes += str(i) + ", "
    # Return all prime numbers as a string
    return primes

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# 4. Create a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page ("/").
#     2. Accepts an integer from the URL (e.g., /7).
#     3. Generates and returns the first N Fibonacci numbers, where N is the integer passed in the URL.

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    # Message asking user to enter a number in the URL
    return "Please add a number to the URL, like /5 or /10"

# Route that accepts an integer from the URL
@app.route("/<int:number>")
def fibonacci(number):
    # String to hold Fibonacci numbers
    fibs = "First " + str(number) + " Fibonacci numbers: "
    # Initialize first two Fibonacci numbers
    fib1, fib2 = 0, 1
    # Generate Fibonacci sequence
    for i in range(number):
        fibs += str(fib1) + ", "
        fib1, fib2 = fib2, fib1 + fib2
    # Return the Fibonacci sequence as a string
    return fibs

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# 5. Create a Flask application that:
#     1. Displays a message "Please add a number to the URL, like /5 or /10" when a user visits the home page (/).
#     2. Accepts an integer from the URL (e.g., /6).
#     3. Calculates the factorial of the given number and displays the result in the browser.

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    # Message asking user to enter a number in the URL
    return "Please add a number to the URL, like /5 or /10"

# Route that accepts an integer from the URL
@app.route("/<int:number>")
def factorial(number):
    # Calculate factorial
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    # Return the factorial result as a string
    return f"Factorial of {number} is: {fact}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# 6. Create a Flask application to navigate between multiple links in a webpage.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/social')
def social():
    return render_template('social.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/social">Social</a>
    </nav>
    <h1>Hello...</h1>
    <p>This is the Home Page.</p>
</body>
</html>
```

```html
<!-- templates/about.html -->
<!DOCTYPE html>
<html>
<head>
    <title>About Page</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/social">Social</a>
    </nav>
    <h1>About Us</h1>
    <p>This is the About Page.</p>
</body>
</html>
```

```html
<!-- templates/social.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Social Media Links</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/social">Social</a>
    </nav>
    <h1>Our Logo:</h1>
    <img src="image_path.jpg" alt="Logo">
</body>
</html>
```

```python
# 7. Write a Flask app with a /contact page containing a form (Name, Message) and a /submit route that displays the submitted data using both POST and GET methods.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact')
def contact():
    return render_template('contacts.html')

# Route to handle form submission
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
        msg = request.form['message']
    else:
        name = request.args.get('username')
        msg = request.args.get('message')

    return f"<h2>Thanks, {name}!</h2><p>Your message: {msg}</p>"

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/contacts.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Page</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit" method="POST">
        <label>Name:</label>
        <input type="text" name="username"><br><br>
        <label>Message:</label>
        <input type="text" name="message"><br><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
```

```python
# 8. Create a Flask application that connects to a MySQL database flaskdb containing a table users(id, name, email).

import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskdb"
)

cursor = db.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

@app.route('/createuser', methods=['
```
