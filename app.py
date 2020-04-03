from flask import Flask, render_template, request
import sys

from models import Register, Authenticater

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', msg='')

@app.route("/post", methods=['POST'])
def post():
    content = request.form['content']
    password = request.form['password']

    print(content, password, file=sys.stderr)

    auth = Authenticater(password)

    if auth.auth():
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
