# Hello World App

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World.<h1>"

@app.route('/second')
def second():
    return "<h2>This is the second page.<h2>"

@app.route('/third/subthird')
def third():
    return "<h3>This is the subpage of third page.<h3>"

@app.route('/forth/<string:id>')
def forth(id):
    if id.isdigit():
        return f"<h3>the id of this page is {id}<h3>"
    else:
        return f"<h3>not a valid page id!<h3>"
    
@app.route('/fifth')
def fifth():
    return '<a href="/third/subthird">to subthird</a>'


# Run the Flask App
app.run(debug=False)

