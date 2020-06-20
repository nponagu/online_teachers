from flask_sqlalchemy import SQLAlchemy, Column, Integer, String, Text, Float, JSON, DateTime, ForeignKey
from flask_sqlalchemy.orm import relationship

from app import app


conf = json.load(open('pass_db.json', 'r', encoding='utf-8'))[0]
login = conf.get("login")
pwd = conf.get("pwd")
db_connection = f'postgresql://{login}:{pwd}@localhost/online_studying'


app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
db = SQLAlchemy(app)


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    about = db.Column(db.Text)
    rating = db.Column(db.Float)
    picture = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    free = db.Column(db.JSON)
    boolings = db.relationship("Booking")


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    clientName = db.Column(db.String(50), nullable=False)
    clientPhone = db.Column(db.String(15), nullable=False)
    clientTime = db.Column(db.DateTime, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    teacher = db.relationship("Teacher")
