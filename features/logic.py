from flask import Blueprint, render_template, request

logic = Blueprint('logic', __name__)


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
