from flask import Flask, render_template, request, jsonify
from models import Register, Authenticater
from tweet import tweet

import sys, os

app = Flask(__name__)

SLACK_TOKEN = os.environ['SLACK_TOKEN']

HOST = os.environ['HOST']
PORT = os.environ['PORT']
PORT = int(PORT)

@app.route("/", methods=['GET', 'POST'])
def index():
    msg = ''

    if request.method == 'GET':
        token = request.args.get("token", default='')
        if not token:
            msg = 'トークンがありません。<br>ツイートするにはあかこうにトークンをもらって下さい。'

    elif request.method == 'POST':
        content = request.form['content']
        token = request.form['token']

        auth = Authenticater(token)

        if auth.auth():
            print(f'content:{content}\ntoken:{token}\n')
            tweet(content)

            msg = '送信しました'
            auth.destroy()
            token = ''
        else:
            msg = '認証に失敗しました'

    return render_template('index.html', msg=msg, token=token)


@app.route("/generate_token", methods=['POST'])
def generate_token():
    if request.form['token'] != SLACK_TOKEN:
        return jsonify({})

    register = Register()
    token = register.register()

    url = f'{HOST}?token={token.token}'

    return jsonify({'text': url})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT)
