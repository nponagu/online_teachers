from app import db


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    about = db.Column(db.Text)
    rating = db.Column(db.Float)
    picture = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Text)
    free = db.Column(db.JSON)
    bookings = db.relationship("Booking")


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    clientName = db.Column(db.String(50), nullable=False)
    clientPhone = db.Column(db.String(15), nullable=False)
    clientTime = db.Column(db.String(5), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    teacher = db.relationship("Teacher")


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    clientName = db.Column(db.String(50), nullable=False)
    clientPhone = db.Column(db.String(15), nullable=False)
    goal = db.Column(db.Text)
    time = db.Column(db.String(5))


db.create_all()