from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    with open('static/user/user', mode='r', encoding='utf-8') as file:
        infos = file.readlines()
    for info in infos:
        username = info.strip().split('|')[0]
        password = info.strip().split('|')[1]
        if username == data.get('username') and password == data.get('password'):
            return render_template('index.html')
    return render_template('register.html')


@app.route('/register_write_in', methods=['POST'])
def register_write_in():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    with open('static/user/user', mode='a', encoding='utf-8') as file:
        file.write(username + '|' + password + '\n')
    return render_template('login.html')
