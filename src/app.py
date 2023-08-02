from flask import Flask, request, render_template
from ext import config
from ext import database

app = Flask(__name__)
config.init(app)
database.init(app)



# ROUTES
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()