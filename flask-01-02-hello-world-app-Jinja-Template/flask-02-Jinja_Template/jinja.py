# Using Jinja templates

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=2, number2=20)

@app.route("/sum/<string:a>/<string:b>")
def number(a, b):
    if a.isdigit() and b.isdigit():
        total = int(a) + int(b)
        return render_template("body.html", num1 = a, num2 = b, sum = total)
    else:
        return "Invalid Numbers!"


@app.route("/numbers/<string:num1>/<string:num2>")
def custom(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return render_template("index.html", number1=num1, number2=num2)
    else:
        return "Invalid Numbers!"

app.run(debug=False)