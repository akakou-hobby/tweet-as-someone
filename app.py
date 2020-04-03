from flask import Flask, render_template, request
from models import Register, Authenticater

import sys, os

app = Flask(__name__)

PASSWORD = os.environ['USER_PASSWORD']


@app.route("/")
def index():
    return render_template('index.html', msg='')

@app.route("/post", methods=['POST'])
def post():
    content = request.form['content']
    password = request.form['password']
    token = request.form['token']

    print(content, token,  password, file=sys.stderr)
    auth = Authenticater(token)

    if auth.auth() and password == PASSWORD:
        msg = '送信しました'
        auth.destroy()
    else:
        msg = '認証に失敗しました'

    return render_template('index.html', msg=msg)

@app.route("/generate_token")
def generate_token():
    register = Register()
    token = register.register()
    return token.token

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000)
