
from flask import Blueprint, redirect, url_for, render_template, request
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слеша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слешем'


@lab2.route('/lab2/example')
def example():
    name, name_title, group, lab_num, number_course = 'Алина Терехова', 'Терехова Алина', 'ФБИ-24', 2, 3
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 120},
        {'name': 'Апельсины', 'price': 80},
        {'name': 'Мандарины', 'price': 95},
        {'name': 'Манго', 'price': 321},
    ]
    return render_template('example.html', name = name, group=group,
                           lab_num = lab_num, number_course=number_course, name_title=name_title,
                            fruits=fruits )
 

@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')
 

@lab2.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:num1>/<int:num2>')
def calc(num1, num2):
    sum_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2
    div_result = "Деление на ноль невозможно" if num2 == 0 else num1 / num2
    pow_result = num1 ** num2
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Расчет с параметрами </h1>
    <p>{num1} + {num2} = {sum_result}</p>
    <p>{num1} - {num2} = {sub_result}</p>
    <p>{num1} * {num2} = {mul_result}</p>
    <p>{num1} / {num2} = {div_result}</p>
    <p>{num1} <sup> {num2} </sup>= {pow_result}</p>
    </body>
</html>
'''


@lab2.route('/lab2/calc/')
def redirect_to_default():
    return redirect('lab2/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def redirect_with_default_b(a):
    return redirect(f'lab2/lab2/calc/{a}/1')


book_list = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Гарпер Ли", "title": "Убить пересмешника", "genre": "Роман", "pages": 281},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Дж. Р. Р. Толкин", "title": "Властелин колец", "genre": "Фэнтези", "pages": 1216},
    {"author": "Рей Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Фантастика", "pages": 194},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Сказка", "pages": 96},
    {"author": "Дэниел Киз", "title": "Цветы для Элджернона", "genre": "Фантастика", "pages": 311},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 504},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Поэма", "pages": 384}
]

@lab2.route('/lab2/books')
def show_books():
    return render_template('lab2/books.html', books=book_list)


arts = [
    {"name": "Заросший пруд", "description": "«Заросший пруд» — пейзаж русского художника Василия Поленова, написанный в 1879 году.Этот замечательный пейзаж знакомит нас со старым заросшим прудиком, наполненным тиной и листвой от стоящих рядом деревьев. Тишина, отсутствие шума и суеты, тёплая летняя зелень.", "image": "pryd.webp"},
    {"name": "У омута", "description": "«У омута» — пейзаж русского художника Исаака Левитана, написанный в 1892 году.На переднем плане полотна изображены мостки, переходящие в брёвна плотины, справа от которой находится омут. На другой стороне реки продолжается узкая тропинка.", "image": "omyt.webp"},
    {"name": "Корабельная роща", "description": "Афонасовская корабельная роща близ Елабуги» - последнее крупное произведение И. И. Шишкина, его «лебединая песня». Оно создано художником в 1898 году и является обобщением творческого и жизненного опыта художника, всех знаний, которые он накопил за немалую творческую жизнь.", "image": "rocha.jpg"},
    {"name": "Берёзовая роща", "description": "Считается, что замысел картины был подсказан Шишкину известным художником Савицким К. А. Рукой именно этого художника, кстати, были написаны медведица и играющие медвежата. Однако Третьяков, который приобрел полотно, решил закрепить за ним авторство Шишкина, поскольку считал, что основная работа сделана именно им.", "image": "ytro.jpg"},
    {"name": "Сказка о спящей царевне", "description": "Картина «Сказка о спящей царевне» уносит зрителя в волшебный мир сказки. Для её написания автор использовал насыщенные и яркие краски преимущественно тёплых тонов, поэтому, смотря на картину, сразу ощущается необычность, сказочность происходящего.", "image": "ckazka.jpg"}

]

@lab2.route('/lab2/arts')
def show_arts():
    return render_template('lab2/art.html', arts=arts)


flower_data = [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 100},
    {'name': 'Незабудка', 'price': 50},
    {'name': 'Ромашка', 'price': 75},
]

@lab2.route('/lab2/flowers')
def show_all_flowers():
    return render_template('lab2/flowers.html', flowers=flower_data)


@lab2.route('/lab2/add_flowers', methods=['POST']) # это один из HTTP-методов, используемых для отправки данных от клиента
def add_flowers():  
    name = request.form.get('name')  # Получаем значение поля 'name' из данных формы, отправленных в запросе
    price = request.form.get('price')  # Получаем значение поля 'price' из данных формы, отправленных в запросе
    #request.form.get - это метод из библиотеки Flask, который позволяет извлекать данные, отправленные в теле POST-запроса в виде формы 
    # (например, через HTML-форму).
    if not name or not price:  
        return "Неверные данные", 400  
    flower_data.lab2end({'name': name, 'price': int(price)})  # Добавляем новый цветок в список 'flower_data' с извлечённым именем и
                                                            # ценой (при этом price конвертируем в целое число)
    return redirect(url_for('show_all_flowers')) 


@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id >= len(flower_data):
        return "Такого цветка нет", 404
    del flower_data[flower_id]
    return redirect(url_for('show_all_flowers'))


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_data.clear()
    return redirect(url_for('show_all_flowers'))