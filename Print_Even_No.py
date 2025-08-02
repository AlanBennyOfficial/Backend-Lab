from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:n>')
def even(n):
    even = ""
    for i in range(1,n+1):
        if(i%2==0):
            even +=str(i)+", "
    return even

if __name__ == '__main__':
    app.run(debug=True)
