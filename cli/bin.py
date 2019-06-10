import os
import sys
from flask import Flask
from flask import jsonify
from .parse import parseUser, parsePages

app = Flask(__name__)
filename = os.path.abspath(sys.argv[1])

with open(filename, 'r') as file:
    text = file.read()

userinfo = parseUser(text)
pages = parsePages(text)


@app.route("/")
def user():
    return str(pages)


def main():
    app.run()


if __name__ == "__main__":
    main()
