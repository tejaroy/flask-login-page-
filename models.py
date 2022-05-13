from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__= "user"

    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(25),nullable=False)
    username=db.Column(db.String(25),unique=True,nullable=False)
    email=db.Column(db.String(25),unique=True,nullable=False)
    pwd=db.Column(db.String(30),unique=True,nullable=False)

    def __repr__(self):
        return '<User %r>' %self.username
