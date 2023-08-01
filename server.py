from flask import Flask, request, render_template

app = Flask(__name__)
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

@app.route('/')
def home():
    return render_template('index.html', files=values)

app.run(debug=1)
