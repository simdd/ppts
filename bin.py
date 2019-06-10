import os
import sys
import subprocess
from flask import Flask
from flask import jsonify
from parse import parseUser, parsePages

app = Flask(__name__)
filename = os.path.abspath(sys.argv[1])

with open(filename, 'r') as file:
    text = file.read()

userinfo = parseUser(text)
pages = parsePages(text)


@app.route("/")
def user():
    return str(pages)


def startWeb():
    subprocess.call(["yarn", "start"])


def main():
    app.run()
    startWeb()


if __name__ == "__main__":
    main()
    startWeb()
