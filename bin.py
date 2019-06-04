from flask import Flask
from flask import jsonify
from parse import parseUser
app = Flask(__name__)

with open('demo.ppts', 'r') as file:
    text = file.read()

userinfo = parseUser(text)


@app.route("/")
def user():
    return jsonify(userinfo)


if __name__ == "__main__":
    app.run()
