from flask import Blueprint, render_template, redirect, url_for

lab2 = Blueprint('lab2', __name__)

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/a/')
def a():
    return 'со слешем'

@lab2.route('/lab2/a')
def a2():
    return 'без слеша'

@lab2.route('/lab2/flowers/<int:flower_id>')
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
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
                <title>Информация о цветке</title>
            </head>
            <body>
                <h1>Информация о цветке</h1>
                <p>Цветок: ''' + flower + '''</p>
                <p><a href="''' + url_for('lab2.all_flowers') + '''">Посмотреть все цветы</a></p>
            </body>
        </html>
        '''

@lab2.route('/lab2/add_flower/<string:name>')
def add_flower(name):
    flower_list.append(name)
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
            <title>Добавление цветка</title>
        </head>
        <body>
            <h1>Добавление цветка</h1>
            <p>Название нового цветка: ''' + name + '''</p>
            <p>Всего цветков: ''' + str(len(flower_list)) + '''</p>
            <p>Список цветков: ''' + str(flower_list) + '''</p>
            <p><a href="''' + url_for('lab2.all_flowers') + '''">Посмотреть все цветы</a></p>
        </body>
    </html>
    '''

@lab2.route('/lab2/add_flower/')
def add_flower_error():
    return 'вы не задали имя цветка', 400

@lab2.route('/lab2/all_flowers')
def all_flowers():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
            <title>Все цветы</title>
        </head>
        <body>
            <h1>Все цветы</h1>
            <p>Количество цветов: ''' + str(len(flower_list)) + '''</p>
            <p>Список цветов: ''' + str(flower_list) + '''</p>
            <p><a href="''' + url_for('lab2.clear_flowers') + '''">Очистить список цветов</a></p>
        </body>
    </html>
    '''

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    return '''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
            <title>Очистка списка цветов</title>
        </head>
        <body>
            <h1>Список цветов очищен</h1>
            <p><a href="''' + url_for('lab2.all_flowers') + '''">Посмотреть все цветы</a></p>
        </body>
    </html>
    '''

@lab2.route('/lab2/example')
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

@lab2.route('/lab2/')
def lab2_main():
    fruits = [
        {'name': 'Яблоко', 'price': 50},
        {'name': 'Банан', 'price': 30},
        {'name': 'Апельсин', 'price': 40}
    ]
    return render_template('lab2.html', fruits=fruits)  

@lab2.route('/lab2/filter')
def filter_example():
    phrase = "сколько нам открытий чудных готовит просвещенья дух"
    return render_template('filter.html', phrase=phrase)

# Обработчик для перенаправления с /lab2/calc/ на /lab2/calc/1/1
@lab2.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('lab2.calc', a=1, b=1))

# Обработчик для перенаправления с /lab2/calc/<int:a> на /lab2/calc/<int:a>/1
@lab2.route('/lab2/calc/<int:a>')
def redirect_calc(a):
    return redirect(url_for('lab2.calc', a=a, b=1))

# Основной обработчик, который выполняет математические операции
@lab2.route('/lab2/calc/<int:a>/<int:b>')
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

@lab2.route('/lab2/books/')
def index():
    return render_template('books.html', books=books)

cats = [
    {"name": "Мурка", "description": "Спокойная и ласковая кошка.", "image": "cat1.jpg"},
    {"name": "Барсик", "description": "Активный и игривый кот.", "image": "cat2.jpg"},
    {"name": "Пушок", "description": "Любит спать весь день.", "image": "cat3.jpg"},
    {"name": "Снежок", "description": "Просто душка.", "image": "cat4.jpg"},
    {"name": "Рыжик", "description": "Пушистая прелесть.", "image": "cat5.jpg"},
]

@lab2.route('/lab2/cats/')
def cat():
    return render_template('lab2/cats.html', cats=cats)