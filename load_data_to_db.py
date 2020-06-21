import json

from app import db
from models import Teacher, Booking, Request


teachers_records = json.load(open('mock_db.json', 'r', encoding='utf-8'))[1]
teachers = []
for record in teachers_records:
    goals = " ".join([x for x in record.get("goals")])
    print(goals)
    teacher = Teacher(name = record.get("name"),
                      about = record.get("about"),
                      rating = record.get("rating"),
                      picture = record.get("picture"),
                      price = record.get("price"),
                      goals = goals,
                      free = record.get("free"))
    teachers.append(teacher)


book_records = json.load(open('booking.json', 'r', encoding='utf-8'))
bookings = []
for record in book_records:
    booking = Booking(clientName = record.get("clientName"),
                      clientPhone = record.get("clientPhone"),
                      clientTime = record.get("clientTime"),
                      teacher_id = record.get("clientTeacher")
    )
    bookings.append(booking)


request_records = json.load(open('request.json', 'r', encoding='utf-8'))
requests = []
for record in request_records:
    request = Request(clientName = record.get("clientName"),
                      clientPhone = record.get("clientPhone"),
                      goal = record.get("goal"),
                      time = record.get("time")
    )
    requests.append(request)


db.session.add_all(bookings)
db.session.add_all(teachers)
db.session.add_all(requests)
db.session.commit()