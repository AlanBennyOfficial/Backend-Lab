from flask import Flask#, render_template

app = Flask(__name__)

@app.route('/<int:n>')
def Fib(n):
    n1, n2, n3 = 0, 1, 1
    fibList = ""

    for _ in range(n):
        fibList += str(n1)+ ", "
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return fibList

if __name__ == '__main__':
    app.run(debug=True)
