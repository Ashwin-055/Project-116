# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    return render_template('index.html',title="His info",relation="He",name="Sundar Pichai",age="50",image="static/me.jpg")

@app.route("/father")
def fat():
    return render_template('index.html',title="His father's info",relation="His father",name="Regunatha Pichai",age="150",image="static/father.jpg")

@app.route("/mother")
def mot():
    return render_template('index.html',title="His mother's info",relation="His mother",name="Lakshmi Pichai",age="140",image="static/mother.jpeg")

@app.route("/friend")
def fri():
    return render_template('index.html',title="His friend's info",relation="His friend",name="Larry Page",age="50",image="static/friend.jpg")

if __name__  ==  '__main__':
    app.run(debug=True)