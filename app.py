"""
    Author : Atharva Mane
    Date : 18 April 2024
    Languages : HTML , CSS , BootStrap ,  Python , Flask , SQLAlchemy
    Hosted : https://atharvamane.pythonanywhere.com/

    To create todo table(if not created) fire this commands in cmd/powershell
    from app import app,db
    with app.app_context():
        db.create_all() 

"""
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
app.app_context().push()

#Database Class
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.task} - {self.status}"

# Main Page
@app.route("/")
def index():
    data = Todo.query.all()
    return render_template('index.html',data=data)

# Addd Record
@app.route("/task", methods=['POST'])
def taskData():
    if request.method == 'POST':
        task = request.form['task']
        todo = Todo(task=task)
        db.session.add(todo)
        db.session.commit()

    data = Todo.query.all()
    print(data)
    return render_template('index.html',data=data)

# Delete Record
@app.route('/delete/<int:sno>')
def removeTask(sno):
    task = Todo.query.filter_by(sno=sno).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

# Check (Task Done or not status)
@app.route('/check/<int:sno>')
def check(sno):
    task = Todo.query.filter_by(sno=sno).first()
    task.status = not task.status
    db.session.commit()
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug=True)