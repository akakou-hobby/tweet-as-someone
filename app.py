from flask import Flask, render_template, request
from models import Register, Authenticater

import sys, os

app = Flask(__name__)

USER_PASSWORD = os.environ['USER_PASSWORD']
HOST = os.environ['HOST']

@app.route("/", methods=['GET', 'POST'])
def index():
    msg = ''

    if request.method == 'GET':
        token = request.args.get("token", default='')

    elif request.method == 'POST':
        content = request.form['content']
        token = request.form['token']

        auth = Authenticater(token)

        if auth.auth():
            msg = '送信しました'
            auth.destroy()
            token = ''
        else:
            msg = '認証に失敗しました'

    return render_template('index.html', msg=msg, token=token)


@app.route("/generate_token")
def generate_token():
    register = Register()
    token = register.register()
    return f'{HOST}?token={token.token}'

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000)
