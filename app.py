from flask import Flask, redirect, url_for, render_template

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


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'нет цветка', 404
    else:
        flower = flower_list[flower_id]
        return '''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
                <title>Информация о цветке</title>
            </head>
            <body>
                <h1>Информация о цветке</h1>
                <p>Цветок: ''' + flower + '''</p>
                <p><a href="''' + url_for('all_flowers') + '''">Посмотреть все цветы</a></p>
            </body>
        </html>
        '''

@app.route('/lab2/add_flower/<string:name>')
def add_flower(name):
    flower_list.append(name)
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            <title>Добавление цветка</title>
        </head>
        <body>
            <h1>Добавление цветка</h1>
            <p>Название нового цветка: ''' + name + '''</p>
            <p>Всего цветков: ''' + str(len(flower_list)) + '''</p>
            <p>Список цветков: ''' + str(flower_list) + '''</p>
            <p><a href="''' + url_for('all_flowers') + '''">Посмотреть все цветы</a></p>
        </body>
    </html>
    '''

@app.route('/lab2/add_flower/')
def add_flower_error():
    return 'вы не задали имя цветка', 400

@app.route('/lab2/all_flowers')
def all_flowers():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            <title>Все цветы</title>
        </head>
        <body>
            <h1>Все цветы</h1>
            <p>Количество цветов: ''' + str(len(flower_list)) + '''</p>
            <p>Список цветов: ''' + str(flower_list) + '''</p>
            <p><a href="''' + url_for('clear_flowers') + '''">Очистить список цветов</a></p>
        </body>
    </html>
    '''

@app.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            <title>Очистка списка цветов</title>
        </head>
        <body>
            <h1>Список цветов очищен</h1>
            <p><a href="''' + url_for('all_flowers') + '''">Посмотреть все цветы</a></p>
        </body>
    </html>
    '''


@app.route('/lab2/example')
def example():
    name = 'Руди Дмитрий Константинович'
    nlab = '2'
    group = '24'
    course = '3'
    fruits = [
        {'name': 'Яблоко', 'price': 50},
        {'name': 'Банан', 'price': 30},
        {'name': 'Апельсин', 'price': 40}
    ]
    return render_template('example.html', name=name, nlab=nlab, group=group, course=course, fruits=fruits)  

@app.route('/lab2/')
def lab2():
    fruits = [
        {'name': 'Яблоко', 'price': 50},
        {'name': 'Банан', 'price': 30},
        {'name': 'Апельсин', 'price': 40}
    ]
    return render_template('lab2.html', fruits=fruits)  

@app.route('/lab2/filter')
def filter_example():
    phrase = "сколько нам открытий чудных готовит просвещенья дух"
    return render_template('filter.html', phrase=phrase)