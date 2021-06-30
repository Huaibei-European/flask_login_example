"""
通过蓝图分包的方式实现分别展示html页面的逻辑和处理登录注册的逻辑。
The logic of displaying html pages and the logic of processing
login and registration are realized by blueprint subcontracting.
"""
from flask import Flask
from features import logic, html

app = Flask(__name__)

app.register_blueprint(html.html)
app.register_blueprint(logic.logic)
