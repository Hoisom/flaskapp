from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

app.run(debug=True)