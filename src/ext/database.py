from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))

def init(app):
    db.init_app(app)