from flask import Flask,jsonify,request
import databasePort
app = Flask(__name__)

'''Use Post Save Information'''
@app.route('/usersInformation',methods=['POST'])
def saveUserInfoAndBackuserId():
    get_username = request.json['username']
    get_password = request.json['password']
    databasePort.addUser(get_username,get_password)
    return jsonify([{'status':'ok'}])

@app.route('/talks',methods=['POST'])
def saveUserTalk():
    get_content = request.json['talkContent']
    get_date = request.json['talkDate']
    get_location = request.json['talkLocation']
    get_uerId = request.json['userId']
    databasePort.addTalk(0,0,get_content,get_uerId,get_date,get_location)
    return jsonify([{'status':'ok'}])

@app.route('/comments',methods=['POST'])
def saveUnknownComment():
    get_talkId = request.json['talkId']
    get_content = request.json['commentContent']
    get_date = request.json['commentDate']
    databasePort.addComment(get_talkId,get_content,get_date)
    return jsonify([{'status':'ok'}])

@app.route('/diarys',methods=['POST'])
def saveUserDiary():
    get_mood = request.json['mood']
    get_content = request.json['content']
    get_weather = request.json['weather']
    get_date = request.json['date']
    get_userId = request.json['userId']
    databasePort.addDiary(get_mood,get_content,get_weather,get_date,get_userId)
    return jsonify([{'status':'ok'}])

@app.route('/postGood',methods=["POST"])
def saveGood():
    get_talkId = request.json['talkId']
    databasePort.receiveGood(get_talkId)
    return jsonify([{'status':'ok'}])


'''Use GET Gain the Information from mysql'''
@app.route('/userLogin',methods=["POST"])
def userLogin():
    get_username = request.json['username']
    get_password = request.json['password']
    return jsonify([{'userId':databasePort.checkUserInformation(get_username,get_password)}])

@app.route('/getUserDiarys/<userId>',methods=['GET'])
def getUserDiarys(userId):
    return jsonify(databasePort.returnUserDiarys(userId=userId))

@app.route('/getUserTalks/<userId>',methods=["GET"])
def getUserTalks(userId):
    return jsonify(databasePort.returnUserTalks(userId))

@app.route('/getTalkComments/<talkId>')
def getTalkComments(talkId):
    return jsonify(databasePort.returnSoleComments(talkId))

@app.route('/getTalkFromLocation/<location>')
def getLocationTalk(location):
    return jsonify(databasePort.returnLocationTalks(location))


'''对管理者开放'''
@app.route('/managedb')
def createAndDrop():
    databasePort.drop_db()
    databasePort.create_db()
    return 0

if __name__ == '__main__':
    app.run()
