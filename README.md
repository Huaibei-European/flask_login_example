# flask_login_example

这是一个利用flask实现简易登录的代码，通过不同类型的代码格式，实现不同类型的登录方式，建议从app——appx开始阅读，以便深入了解flask的工作方式。

本代码没用使用数据库操作。

通过文件读写的方式实现记录用户信息的方式。

#### 安装依赖

```
pip install flask
pip install python-dotenv
```

#### 配置启动文件

`.flaskenv`

```
FLASK_ENV=development
FLASK_RUN_PORT = 5000
FLASK_RUN_HOST = 127.0.0.1
FLASK_APP=app.py
```

#### 启动程序

```
flask run
```
