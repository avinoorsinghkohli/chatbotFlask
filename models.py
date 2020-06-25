from app import db

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(1000),nullable=False)
    date=db.Column(db.Date,nullable=False)
    def __repr__(self): # function that shows the return string when any object in db is ref
        return f'{self.title} created by {self.date}'