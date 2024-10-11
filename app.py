from flask import Flask, redirect, url_for

app = Flask(__name__)

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

@app.route('/lab1')
def lab1():
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
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>

        <a href="/menu">Вернуться в меню</a>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/student">Студент</a></li>
            <li><a href="/lab1/python">Python</a></li>
            <li><a href="/lab1/oak">Дуб</a></li>
        </ul>

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>Руди Дмитрий Константинович</h1>
        <img src="''' + url_for('static', filename='nstu_logo.webp') + '''" alt="Лого НГТУ">

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Python</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <div>
            Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.
        </div>

        <div>
            Python поддерживает несколько парадигм программирования, включая структурное, объектно-ориентированное, функциональное, императивное и аспектно-ориентированное программирование. Он имеет большую и всеобъемлющую стандартную библиотеку.
        </div>

        <div>
            Python является интерпретируемым языком, поддерживающим динамическую типизацию. Это означает, что переменные в Python не требуют объявления типа данных, и тип может изменяться во время выполнения программы.
        </div>

        <img src="''' + url_for('static', filename='python_logo.webp') + '''" alt="Лого Python">

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''

@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Дуб</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>ДУБ</h1>
        <img src="''' + url_for('static', filename='oak.webp') + '''" alt="Дуб">

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''

@app.route('/lab2/a/')
def a():
    return 'со слешем'
@app.route('/lab2/a')
def a2():
    return 'без слеша'
