# flask_login_example

这是一个利用flask实现简易登录的代码，通过不同类型的代码格式，实现不同类型的登录方式，建议从app——appx开始阅读，以便深入了解flask的工作方式。

本代码没用使用数据库操作。

通过文件读写的方式实现记录用户信息的方式。

请在虚拟环境下创建。如何创建虚拟环境？请看https://github.com/Huaibei-European/python_create_virtual_environment

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

</br>
</br>
</br>

This is a code that uses flash to realize simple login. 

Different types of login methods can be realized through different types of code formats. 

It is recommended to start reading from app -- appx, so as to have an in-depth understanding of how flash works.

This code does not use the database operation.

Through the way of file reading and writing to realize the way of recording user information.

Please create it in a virtual environment. How to create a virtual environment? Look https://github.com/Huaibei-European/python_create_virtual_environment

#### Installation dependency
```
pip install flask
pip install python-dotenv
```

#### Configure startup file
`.flaskenv`

```
FLASK_ ENV=development
FLASK_ RUN_ PORT = 5000
FLASK_ RUN_ HOST = 127.0.0.1
FLASK_ APP=app.py
```

#### Start the program
```
flask run
```
