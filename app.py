from flask import Flask, redirect, url_for
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_user = 'alina_terehova_orm'
    db_password = '1234'
    db_name = 'alina_terehova_orm'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "alina_terehova_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)


app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)


@app.route("/")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href=' """ + url_for('static', filename='lab1/main.css') + """ ' }}">
    </head>
    <body>
        <header>
           
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <div>
        <h1> Меню</h1> 
        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li> 
                <li><a href="/lab3">Третья лабораторная</a></li> 
                <li><a href="/lab4">Четвертая лабораторная</a></li>
                <li><a href="/lab5">Пятая лабораторная</a></li>  
                <li><a href="/lab6">Шестая лабораторная</a></li>  
                <li><a href="/lab7">Седьмая лабораторная</a></li>  
                <li><a href="/lab8">Восьмая лабораторная</a></li>  
                <li><a href="/lab9">Девятая лабораторная</a></li> 
            </ul>
        </nav>
        </div>

        <footer> 
            &copy; Алина Терехова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """




@app.errorhandler(404)
def not_found(err):
    css_err = url_for("static", filename="lab1/err.css")
    img_err = url_for("static", filename="lab1/404.png")
    return f'''
        <!doctype html>
        <html>
            <head>
                <title>Страница не найдена</title>
                <link rel="stylesheet" href="{css_err}">
            </head>
            <body>
                <h1>Страница не найдена</h1>
                <p>К сожалению, запрашиваемая Вами страница не была найдена.</p>
                <p>Вы можете перейти на <a href="/">главную страницу</a> или попробовать воспользоваться поиском.</p>
                <img src="{img_err}">
            </body>
        </html>''', 404


@app.errorhandler(500)
def server_error(err):
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Внутренняя ошибка сервера</title>
            </head>
            <body>
                <h1>Произошла внутренняя ошибка сервера</h1>
                <p>
                    Приносим свои извинения за неудобства. Пожалуйста, попробуйте обновить страницу или вернуться позже.
                </p>
            </body>
        </html>''', 500