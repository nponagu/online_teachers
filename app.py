from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/goals/<goal>/')
def render_goal(goal):
    return 'Hello Moon!'


@app.route('/profiles/<int:teacher_id>/')
def render_profile(teacher_id):
    return 'Hello World!'


@app.route('/request/')
def render_request():
    return 'Hello World!'


@app.route('/request_done/')
def render_request_done():
    return 'Hello World!'


@app.route('/booking/<int:teacher_id>/<int:day>/<time>/')
def render_booking(teacher_id, day, time):
    return 'Hello World!'


@app.route('/booking_done/')
def render_booking_done():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
