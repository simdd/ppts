import os
from flask import Flask
from flask import jsonify
from parse import parseUser, parsePages

app = Flask(__name__)
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'demo.ppts')

with open(filename, 'r') as file:
    text = file.read()

userinfo = parseUser(text)
pages = parsePages(text)


@app.route("/")
def user():
    return str(pages)


if __name__ == "__main__":
    app.run()
