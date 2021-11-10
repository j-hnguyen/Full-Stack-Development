from flask import Flask, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'
app.config['SECRET_KEY'] = "jackieIsCool"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

class STUDENTGRADE(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, unique=True, nullable=False)
   grade = db.Column(db.String, nullable=False)

def returnAll():
    json = {}
    for student in STUDENTGRADE.query.all():
        json[student.name] = student.grade
    return json

@app.route('/grades', methods=["GET", "POST"])
def grades():
    if request.method == "GET":
        return(returnAll())
    if request.method == "POST":
        content = request.get_json()
        db.session.add(STUDENTGRADE(name=content['name'], grade=content['grade']))
        db.session.commit()
        return(returnAll())

@app.route('/grades/<name>', methods=["GET", "PUT", "DELETE"])
def gradesSingleStudent(name):
    student = STUDENTGRADE.query.filter_by(name=name).first()
    if request.method == "GET":
        return {student.name : student.grade}
    if request.method == "PUT":
        student.grade = request.get_json()["grade"]
    elif request.method == "DELETE":
        db.session.delete(student)
        db.session.commit()
        return(returnAll())

if __name__ == "__main__":
    db.create_all()
    app.run()