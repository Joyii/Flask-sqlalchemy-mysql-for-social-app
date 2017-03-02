from dataBase import db,User,Comments,Talks,Diary

'''创建数据库'''
def create_db():
    db.create_all()

'''清空数据库'''
def drop_db():
    db.drop_all()

'''增加数据'''
def addUser(username,password):
    user = User(username,password)
    db.session.add(user)
    db.session.commit()

def addDiary(mood,content,weather,date,userId):
    diary = Diary(mood,content,weather,date,userId=userId)
    db.session.add(diary)
    db.session.commit()

def addTalk(commentNum,goodNum,content,userId,date,location):
    talk = Talks(commentNum,goodNum,content,userId,date,location)
    db.session.add(talk)
    db.session.commit()

''''返回用户所需数据'''
def returnUserDiarys(userId):
    list = []
    results = Diary.query.filter_by(userId = userId).all()
    print(results)
    for i in results:
        dic = {}
        dic["mood"] = i.mood
        dic["weather"] = i.weather
        dic["content"] = i.content
        dic["date"] = i.date
        list.append(dic)
    return list

def returnSoleComments(talkId):
    list = []
    results = Comments.query.filter_by(talkId = talkId).all()
    for i in results:
        dic = {}
        dic["content"] = i.comment_content
        dic["date"] = i.date
        list.append(dic)
    return list

def returnUserTalks(userId):
    list = []
    results = Talks.query.filter_by(userId = userId).all()
    for i in results:
        dic = {}
        dic["content"] = i.content
        dic["location"] = i.location
        dic["talkId"] = i.talkId
        dic["goodNum"] = i.goodNum
        dic["commentNum"] = i.commentNum
        dic["date"] = i.date
        list.append(dic)
    return list

def returnLocationTalks(location):
    list = []
    results = Talks.query.filter_by(location = location).all()
    for i in results:
        dic = {}
        dic["content"] = i.content
        dic["goodNum"] = i.goodNum
        dic["commentNum"] = i.commentNum
        dic["date"] = i.date
        dic["talkId"] = i.talkId
        list.append(dic)
    return list

def checkUserInformation(username,password):
    result = User.query.filter_by(user=username,pas=password).all()
    if result:
        userId = result[0].userId
    else:
        userId = -1
    return userId


'''点赞 评论后的update评论'''
def receiveGood(talkId):
    db.session.execute("UPDATE talks SET goodNum=goodNum+1 WHERE talkId=:param", {"param": talkId})
    db.session.commit()


def addComment(talkId, comment_content, date):
    '''提交评论'''
    comment = Comments(talkId, comment_content, date)
    db.session.add(comment)
    '''同时修改CommentNum'''
    db.session.execute("UPDATE talks SET commentNum=commentNum+1 WHERE talkId=:param",{"param":talkId})
    db.session.commit()
