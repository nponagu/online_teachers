from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def index():
    goals = json.load(open('mock_db.json', 'r', encoding='utf-8'))[0]
    teachers = json.load(open('mock_db.json', 'r', encoding='utf-8'))[1]
    return render_template('index.html', goals=goals, teachers=teachers)


@app.route('/goals/<string:goal>/')
def render_goal(goal):
    return render_template('goal.html')


@app.route('/profiles/<int:teacher_id>/')
def render_profile(teacher_id):
    teachers = json.load(open('mock_db.json', 'r', encoding='utf-8'))[1]
    for item in teachers:
        if item["id"] == teacher_id:
            teacher = item
    print(teacher)

    schedule = teacher["free"]
    return render_template('profile.html', teacher=teacher, schedule=schedule)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    return render_template('request_done.html')


@app.route('/booking/<int:teacher_id>/<int:day>/<time>/')
def render_booking(teacher_id, day, time):
    return render_template('booking.html')


@app.route('/booking_done/')
def render_booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run(debug=True)
