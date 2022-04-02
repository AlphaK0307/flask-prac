from enum import unique
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column (db.String(50), unique= True, nullable=False)
    email= db.Column (db.String(50), unique= True, nullable=False)
    password= db.Column (db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User|{self.username}>"

    def __str__(self):
        return self.username
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(20), unique= True, nullable=False)
    body= db.Column(db.String(255))
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post|{self.title}>"

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(100), unique= True, nullable=False)
    last_name=db.Column(db.String(100), unique= True, nullable=False)
    phone_number=db.Column(db.String(100), unique= True, nullable=False)
    city=db.Column(db.String(15), nullable=False)
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Phone {self.id}|{self.first_name}>"

    def __str__(self):
        return f"""
        FirstName:{self.first_name}
        LastName:{self.last_name}
        Phone:{self.phone_number}
        City:{self.city}
        """

    