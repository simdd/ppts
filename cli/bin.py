from flask import Flask
from flask import jsonify
from parse import parseUser, parsePages
app = Flask(__name__)

with open('demo.ppts', 'r') as file:
    text = file.read()

userinfo = parseUser(text)
pages = parsePages(text)


@app.route("/")
def user():
    return str(pages)


if __name__ == "__main__":
    app.run()
