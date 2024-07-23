from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
