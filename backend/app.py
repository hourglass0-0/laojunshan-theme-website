import os
from flask_sqlalchemy import SQLAlchemy 
import sqlite3
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy import func
import pytz


DATABASE_PATH = 'web202438.sqlite'

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, DATABASE_PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '#@#$1244DDDsswdsf'
Bootstrap(app)
db = SQLAlchemy(app)

# models
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(16))
    messages = db.relationship('Message', backref='user', lazy='dynamic') 

    def __repr__(self):
        return '<User %r>' % self.username


class Message(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)  # 修改这里的类型为 db.DateTime

    def __repr__(self):
        return f'<Message {self.message_id}>'

class TouristGuide(db.Model):
    __tablename__ = 'touristGuide'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    img_url = db.Column(db.Text)

    def __repr__(self):
        return f'<TouristGuide {self.id}>'
    
class Introduction(db.Model):
    __tablename__='introduction'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    
class History(db.Model):
    __tablename__='history'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    
class Environment(db.Model):
    __tablename__='environment'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text)
    content = db.Column(db.Text)
    
class MainAttraction(db.Model):
    __tablename__='mainAttraction'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    description = db.Column(db.Text)
    img_url = db.Column(db.Text)

class NaturalResource(db.Model):
    __tablename__='naturalResource'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)

class TouristAttraction(db.Model):
    __tablename__='touristAttraction'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)

class HistoricalCulture(db.Model):
    __tablename__='historicalCulture'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text)
    content=db.Column(db.Text)
    
# ======================================
# 原生sqlite3连接访问数据库
def select_user(user_name, user_pwd):
    # 连接数据库
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # 执行查询
    cursor.execute("SELECT * FROM users where username='" + user_name + "' and password='" + user_pwd + "'")
    # 获取所有记录
    users = cursor.fetchall()

    # 获取列名
    columns = [description[0] for description in cursor.description]

    user_list = [dict(zip(columns, [field if isinstance(field, bytes) else field for field in row])) for row in users]

    # 关闭数据库连接
    cursor.close()
    conn.close()
    return user_list


# ==============================

# routes
@app.route('/api/login', methods=['GET'])
def login():
    username = request.args.get('userName')
    password = request.args.get('userPwd')
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({"code": 200, "data": [{"id": user.user_id, "username": user.username}], "message": "登录成功"})
    else:
        return jsonify({"code": 200, "data": [{}], "message": "登录失败"})

@app.route('/api/addUser', methods=['POST'])
def add_user():
    username = request.json.get('userName')
    password = request.json.get('userPwd')
    if not username or not password:
        return jsonify({"code": 400, "message": "用户名和密码不能为空"})
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"code": 400, "message": "用户名已存在"})
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"code": 200, "data": [{"id": new_user.user_id, "username": new_user.username}], "message": "注册成功"})


@app.route('/api/postMessage', methods=['POST'])
def post_message():
    username = request.json.get('userName')
    title = request.json.get('title')
    content = request.json.get('content')
    
    if not username or not title or not content:
        return jsonify({"code": 400, "message": "请填写所有字段"})
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"code": 400, "message": "用户不存在"})
    
    # 获取数据库中最大的 message_id
    max_message_id = db.session.query(func.max(Message.message_id)).scalar()
    new_message_id = max_message_id + 1 if max_message_id else 1
    
    # 直接传递当前时间的 datetime 对象
    # timestamp = datetime.utcnow()
    
    # 获取当前时间，并转换为北京时间
    timestamp = datetime.now(pytz.timezone('Asia/Shanghai'))

    
    new_message = Message(message_id=new_message_id, user_id=user.user_id, title=title, content=content, timestamp=timestamp)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"code": 200, "data": {"message_id": new_message.message_id, "title": title, "content": content}, "message": "发表成功"})

@app.route('/api/getMessage', methods=['GET'])
def get_messages():
    try:
        messages = Message.query.all()
        messages_list = []
        for msg in messages:
            messages_list.append({
                'message_id': msg.message_id,
                'author': msg.user.username,  # 使用关联的 User 模型的属性来获取作者名字
                'title': msg.title,
                'content': msg.content,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间戳字符串
            })
        return jsonify(messages_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
# /api/touristGuide 路由
@app.route('/api/touristGuide', methods=['GET'])
def get_tourist_guide():
    try:
        guides = TouristGuide.query.all()
        guides_list = []
        for guide in guides:
            guides_list.append({
                'id': guide.id,
                'title': guide.title,
                'content': guide.content,
                'img_url': guide.img_url
            })
        return jsonify(guides_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/introduction', methods=['GET'])
def get_introduction():
    introductions = Introduction.query.all()
    if introductions:
        introductions_list = [{"id": intro.id, "content": intro.content} for intro in introductions]
        return jsonify({"code": 200, "data": introductions_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})
    
@app.route('/api/history', methods=['GET'])
def get_history():
    histories = History.query.all()
    if histories:
        histories_list = [{"id": history.id, "content": history.content} for history in histories]
        return jsonify({"code": 200, "data": histories_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})
    
@app.route('/api/environment', methods=['GET'])
def get_environment():
    environments = Environment.query.all()
    if environments:
        environments_list = [{"id": environment.id,"title":environment.title, "content": environment.content} for environment in environments]
        return jsonify({"code": 200, "data": environments_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})
    
@app.route('/api/mainAttraction', methods=['GET'])
def get_mainAttraction():
    mainAttractions = MainAttraction.query.all()
    if mainAttractions:
        mainAttractions_list = [{"id": mainAttraction.id,"name":mainAttraction.name, "description": mainAttraction.description,"img_url":mainAttraction.img_url} for mainAttraction in mainAttractions]
        return jsonify({"code": 200, "data": mainAttractions_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})

@app.route('/api/naturalResource', methods=['GET'])
def get_naturalResource():
    naturalResources = NaturalResource.query.all()
    if naturalResources:
        naturalResources_list = [{"id": naturalResource.id, "content": naturalResource.content} for naturalResource in naturalResources]
        return jsonify({"code": 200, "data": naturalResources_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})

@app.route('/api/touristAttraction', methods=['GET'])
def get_touristAttraction():
    touristAttractions = TouristAttraction.query.all()
    if touristAttractions :
        touristAttractions_list = [{"id": touristAttraction.id, "content": touristAttraction.content} for touristAttraction in touristAttractions ]
        return jsonify({"code": 200, "data": touristAttractions_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})

@app.route('/api/historicalCulture', methods=['GET'])
def get_historicalCulture():
    historicalCultures = HistoricalCulture.query.all()
    if historicalCultures :
        historicalCultures_list = [{"id": historicalCulture.id,"title":historicalCulture.title, "content": historicalCulture.content} for historicalCulture in historicalCultures ]
        return jsonify({"code": 200, "data": historicalCultures_list})
    else:
        return jsonify({"code": 404, "message": "未找到相关内容"})

if __name__ == '__main__':
    app.run(debug=True)
    