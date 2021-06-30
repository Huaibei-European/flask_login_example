from flask import Blueprint, render_template, request
import os

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin_manager():
    temp = []
    with open('static/user/user', mode='r', encoding='utf-8') as file:
        infos = file.readlines()
    for info in infos:
        temp.append(
            [
                info.strip().split('|')[0], info.strip().split('|')[1]  # 用户名: 密码
            ]
        )
    print(temp)
    return render_template('admin.html', infos=temp)
