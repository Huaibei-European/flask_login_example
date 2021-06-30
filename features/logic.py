from flask import Blueprint, render_template, request, flash
import copy

logic = Blueprint('logic', __name__)


# 处理登录或注册
@logic.route('/_<parameter>', methods=['POST'])
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
        print(data)
        # 打开文件，查看是否有重名现象
        with open('static/user/user', mode='r', encoding='utf-8') as file:
            infos = file.readlines()
        for info in infos:
            if username == info.strip().split('|')[0]:  # 重名
                return '用户名不可用，请更换用户名！'
        with open('static/user/user', mode='a', encoding='utf-8') as file:
            file.write(username + '|' + password + '\n')
        return 'success'


# 处理修改密码
@logic.route('/modify_password', methods=['POST'])
def modify_password():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    print(data)
    print(username)
    print(password)
    with open('static/user/user', mode='r', encoding='utf-8') as file:
        infos = file.readlines()
    temp = copy.deepcopy(infos)
    print(temp)
    # ['闫明卓|abcd627...\n', '你好|123\n', '你好2号|abcd627...\n']
    for info in infos:
        if username == info.strip().split('|')[0]:
            new_info = username + '|' + password + '\n'
            index = infos.index(info)
            infos.remove(info)
            infos.insert(index, new_info)
    with open('static/user/user', mode='w', encoding='utf-8') as file:
        for info in infos:
            file.write(info)
        return 'success'
