# 2. Create a Flask view that displays a list of hyperlinks to various social media websites using a
#    Jinja template, and map it to a URL route.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/social') 
def social_links():

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