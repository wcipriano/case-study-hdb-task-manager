from project import db, login as login_manager, task_counter
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import event


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Task('{self.content}', '{self.date_posted}', '{self.user_id}')"


def receive_after_insert(mapper, connection, target):
    print(f"*** New event created with ID: {target.id} and Name: {target.content}\n")
    task_counter.inc()

# Event listener
event.listen(Task, 'after_insert', receive_after_insert