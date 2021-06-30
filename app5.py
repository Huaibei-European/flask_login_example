"""
通过蓝图分包的方式实现分别展示html页面的逻辑和处理登录注册的逻辑。
实现后台管理修改密码的界面和逻辑。
The logic of displaying html pages and the logic of processing
login and registration are realized by blueprint subcontracting.
Realize the interface and logic of the background management to modify the password.
"""
from flask import Flask
from features import logic, html, admin

app = Flask(__name__)


class Config:
    SECRET_KEY = 'ymz'


app.config.from_object(Config)

app.register_blueprint(html.html)
app.register_blueprint(logic.logic)
app.register_blueprint(admin.admin)
