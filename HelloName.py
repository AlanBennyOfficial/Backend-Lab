from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    return "Hello %s!" % name

if __name__ == '__main__':
    app.run(debug=True)