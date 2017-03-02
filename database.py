from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hxllovewxh@localhost/myHeart'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer,autoincrement=True,primary_key=True)
    user = db.Column(db.String(20))
    pas = db.Column(db.String(20))

    def __init__(self,username,password):
        self.user = username
        self.pas = password

class Diary(db.Model):
    __tablename__ = 'diarys'
    mood = db.Column(db.String(20))
    content = db.Column(db.Text,)
    userId = db.Column(db.Integer,db.ForeignKey(User.userId,ondelete='CASCADE',onupdate='CASCADE'))
    weather = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    def __init__(self,mood,content,weather,date,userId):
        self.mood = mood
        self.content = content
        self.weather = weather
        self.date = date
        self.userId = userId

class Talks(db.Model):
    __tablename__ = 'talks'
    commentNum = db.Column(db.Integer)
    goodNum = db.Column(db.Integer)
    content = db.Column(db.Text)
    talkId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    usrId = db.Column(db.Integer,db.ForeignKey(User.userId,onupdate='CASCADE',ondelete='CASCADE'))
    date = db.Column(db.DateTime)
    location = db.Column(db.String(20))

    def __init__(self,commentNum,goodNum,content,userId,date,location):
        self.content = content
        self.commentNum = commentNum
        self.goodNum = goodNum
        self.usrId = userId
        self.date = date
        self.location = location

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    talkId = db.Column(db.Integer,db.ForeignKey(Talks.talkId,onupdate='CASCADE', ondelete='CASCADE'));'''用来检索talks'''
    comment_content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self,talkId,comment_content,date):
        self.talkId = talkId
        self.comment_content = comment_content
        self.date = date
