from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def post():
    content = request.form['content']
    password = request.form['password']

    print(content, password, file=sys.stderr)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000)
