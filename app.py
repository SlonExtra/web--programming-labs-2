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

# Обработчик для перенаправления с /lab2/calc/ на /lab2/calc/1/1
@app.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calc', a=1, b=1))

# Обработчик для перенаправления с /lab2/calc/<int:a> на /lab2/calc/<int:a>/1
@app.route('/lab2/calc/<int:a>')
def redirect_calc(a):
    return redirect(url_for('calc', a=a, b=1))

# Основной обработчик, который выполняет математические операции
@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b if b != 0 else "Деление на ноль!"
    pow_result = a ** b

    return f"""
    <h1>Результаты вычислений:</h1>
    <p>Сумма: {a} + {b} = {sum_result}</p>
    <p>Разность: {a} - {b} = {sub_result}</p>
    <p>Произведение: {a} * {b} = {mul_result}</p>
    <p>Деление: {a} / {b} = {div_result}</p>
    <p>Возведение в степень: {a} ^ {b} = {pow_result}</p>
    """



books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Филип Пулман", "title": "Темные начала", "genre": "Фэнтези", "pages": 416},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Харпер Ли", "title": "Убить пересмешника", "genre": "Роман", "pages": 336},
    {"author": "Айн Рэнд", "title": "Атлант расправил плечи", "genre": "Философский роман", "pages": 1168},
    {"author": "Роберт Грин", "title": "48 законов власти", "genre": "Саморазвитие", "pages": 496},
    {"author": "Стивен Кинг", "title": "Оно", "genre": "Ужасы", "pages": 1138},
]

@app.route('/lab2/books/')
def index():
    return render_template('books.html', books=books)

cats = [
    {"name": "Мурка", "description": "Спокойная и ласковая кошка.", "image": "cat1.jpg"},
    {"name": "Барсик", "description": "Активный и игривый кот.", "image": "cat2.jpеg"},
    {"name": "Пушок", "description": "Любит спать весь день.", "image": "cat3.jpg"},
    {"name": "Снежок", "description": "Просто душка.", "image": "cat4.jpg"},
    {"name": "Рыжик", "description": "Пушистая прелесть.", "image": "cat5.jpg"},
]

@app.route('/lab2/cats/')
def cat():
    return render_template('cats.html', cats=cats)
