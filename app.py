import json
from random import sample

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

conf = json.load(open('pass_db.json', 'r', encoding='utf-8'))[0]
login = conf.get("login")
pwd = conf.get("pwd")
db_connection = f'postgresql+psycopg2://{login}:{pwd}@localhost/online_studying'
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection

db = SQLAlchemy(app)
migrate = Migrate(app, db)


week_days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednsday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}


goals = json.load(open('mock_db.json', 'r', encoding='utf-8'))[0]
teachers = json.load(open('mock_db.json', 'r', encoding='utf-8'))[1]


@app.route('/')
def index():

    random_teachers = sample(teachers, 6)

    return render_template('index.html',
                           goals=goals,
                           teachers=random_teachers)


@app.route('/goals/<string:goal>/')
def render_goal(goal):

    selected_teachers = [teacher for teacher in teachers if goal in teacher["goals"]]
    goal_name = goals[goal].lower()

    return render_template('goal.html',
                           teachers=selected_teachers,
                           goal_name=goal_name)


@app.route('/profiles/<int:teacher_id>/')
def render_profile(teacher_id):

    for item in teachers:
        if item["id"] == teacher_id:
            teacher = item

    schedule = teacher["free"]
    return render_template('profile.html',
                           teacher=teacher,
                           schedule=schedule)


@app.route('/request/', methods=['GET', 'POST'])
def render_request():
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def render_request_done():

    goal = goals.get(request.form["goal"])
    time = request.form["time"]
    clientName = request.form["clientName"]
    clientPhone = request.form["clientPhone"]

    req = {"clientName": clientName,
            "clientPhone": clientPhone,
            "goal": goal,
            "time": time}

    with open("request.json", "r+") as file:
        data = json.load(file)
        file.seek(0)
        data.append(req)
        json.dump(data, file)

    return render_template('request_done.html',
                           goal=goal,
                           time=time,
                           clientName=clientName,
                           clientPhone=clientPhone)


@app.route('/booking/<int:teacher_id>/<string:day>/<time>/', methods=['GET', 'POST'])
def render_booking(teacher_id, day, time):

    for item in teachers:
        if item["id"] == teacher_id:
            teacher = item

    week_day = week_days[day]
    time = time

    return render_template('booking.html',
                           teacher=teacher,
                           week_day=week_day,
                           time=time)


@app.route('/booking_done/', methods=['POST'])
def render_booking_done():

    clientName = request.form["clientName"]
    clientPhone = request.form["clientPhone"]
    clientTime = request.form["clientTime"]
    clientTeacher = request.form["clientTeacher"]

    book = {"clientName": clientName,
            "clientPhone": clientPhone,
            "clientTime": clientTime,
            "clientTeacher": clientTeacher}

    with open("booking.json", "r+") as file:
        data = json.load(file)
        file.seek(0)
        data.append(book)
        json.dump(data, file)

    return render_template('booking_done.html',
                           clientName=clientName,
                           clientPhone=clientPhone)


if __name__ == '__main__':
    app.run(debug=True)