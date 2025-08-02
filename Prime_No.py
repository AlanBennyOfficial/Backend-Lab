from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:n>')
def prime(n):
    prime = ""
    for i in range(1, n+1):
        for j in range(2, i):
            if(i%j==0):
                break
            else:
                prime +=str(i)+", "
                break
    return prime

if __name__ == '__main__':
    app.run(debug=True)
