import os
import re
import sys
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)
filename = os.path.abspath(sys.argv[1])

with open(filename, 'r') as file:
    text = file.read()


def parseUser(text):
    reCover = r"--cover--(.*)--cover--"
    reTitle = r"title:\s*([^\n\r]*)\n"
    reAuthor = r"author:\s*([^\n\r]*)\n"
    reDate = r"date:\s*([^\n\r]*)\n"

    cover = re.search(reCover, text, re.S).group(1)
    title = re.search(reTitle, cover, re.S).group(1)
    author = re.search(reAuthor, cover, re.S).group(1)
    date = re.search(reDate, cover, re.S).group(1)

    return {'title': title, 'author': author, 'date': date}


def parsePages(text):
    rePages = r"--page--(.*)--page--"
    pages = re.search(rePages, text, re.S).group(1)
    pages = pages.split('--s--')
    print(pages)
    return pages


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
