from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)

@app.route('/')
@app.route('/index')
def start():
    return redirect("/menu", code=302)

@app.route('/menu')
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Руди Дмитрий Константинович, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='styles.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>
            </ol>
        </div>

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''
