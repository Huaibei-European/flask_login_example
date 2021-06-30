"""
通过蓝图实现分别展示html页面的逻辑和处理登录注册的逻辑。
The logic of displaying the html page and the logic of processing
the login and registration are realized through the blueprint.
"""
from flask import Flask, render_template, request, Blueprint

app = Flask(__name__)

html = Blueprint('html', __name__)
logic = Blueprint('logic', __name__)


@html.route('/')
def login():
    return render_template('login.html')


@html.route('/register')
def register():
    return render_template('register.html')


@logic.route('/<parameter>', methods=['POST'])
def parse_request(parameter):
    if parameter == 'login':
        data = request.form
        with open('static/user/user', mode='r', encoding='utf-8') as file:
            infos = file.readlines()
        for info in infos:
            username = info.strip().split('|')[0]
            password = info.strip().split('|')[1]
            if username == data.get('username') and password == data.get('password'):
                return render_template('index.html')
        return render_template('register.html')
    elif parameter == 'register_write_in':
        data = request.form
        username = data.get('username')
        password = data.get('password')
        with open('static/user/user', mode='a', encoding='utf-8') as file:
            file.write(username + '|' + password + '\n')
        return render_template('login.html')


app.register_blueprint(html)
app.register_blueprint(logic)
