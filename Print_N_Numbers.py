from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    arr = []
    n = 10
    for i in range(0,n):
        arr.append(i)
    return arr

if __name__ == '__main__':
    app.run(debug=True)