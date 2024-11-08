from flask import Blueprint, render_template, request, redirect, session

lab4 = Blueprint('lab4', __name__)

tree_count = 0  # Инициализация счётчика деревьев

users = [
    {'login': 'alex', 'password': '123', 'name': 'Иван Иванов', 'gender': 'male'},
    {'login': 'bob', 'password': '456', 'name': 'Алексей Петров', 'gender': 'male'},
    {'login': 'user1', 'password': 'pass1', 'name': 'Мария Сидорова', 'gender': 'female'},
    {'login': 'user2', 'password': 'pass2', 'name': 'Елена Иванова', 'gender': 'female'}
]

@lab4.route('/lab4')
def lab4_page():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        error = "Оба поля должны быть заполнены"
        return render_template('lab4/div.html', error=error)

    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        error = "Введите корректные числа"
        return render_template('lab4/div.html', error=error)

    if x2 == 0:
        error = "На ноль делить нельзя"
        return render_template('lab4/div.html', error=error)

    result = x1 / x2
    return render_template('lab4/div.html', result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1', 0)
    x2 = request.form.get('x2', 0)

    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        error = "Введите корректные числа"
        return render_template('lab4/sum.html', error=error)

    result = x1 + x2
    return render_template('lab4/sum.html', result=result)

@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1', 1)
    x2 = request.form.get('x2', 1)

    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        error = "Введите корректные числа"
        return render_template('lab4/mul.html', error=error)

    result = x1 * x2
    return render_template('lab4/mul.html', result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        error = "Оба поля должны быть заполнены"
        return render_template('lab4/sub.html', error=error)

    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        error = "Введите корректные числа"
        return render_template('lab4/sub.html', error=error)

    result = x1 - x2
    return render_template('lab4/sub.html', result=result)

@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        error = "Оба поля должны быть заполнены"
        return render_template('lab4/pow.html', error=error)

    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        error = "Введите корректные числа"
        return render_template('lab4/pow.html', error=error)

    if x1 == 0 and x2 == 0:
        error = "Ноль в нулевой степени не определен"
        return render_template('lab4/pow.html', error=error)

    result = x1 ** x2
    return render_template('lab4/pow.html', result=result)

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count

    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'plant' and tree_count < 10:
        tree_count += 1
    elif operation == 'cut' and tree_count > 0:
        tree_count -= 1

    return redirect('/lab4/tree')

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            return render_template('lab4/login.html', authorized=True, login=session['login'], name=session['name'])
        else:
            return render_template('lab4/login.html', authorized=False)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = "Не введён логин"
        return render_template('lab4/login.html', authorized=False, error=error, login=login)

    if not password:
        error = "Не введён пароль"
        return render_template('lab4/login.html', authorized=False, error=error, login=login)

    for user in users:
        if user['login'] == login and user['password'] == password:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')

    error = "Неверный логин или пароль"
    return render_template('lab4/login.html', authorized=False, error=error, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    session.pop('name', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html', temperature=None)

    temperature = request.form.get('temperature')

    if not temperature:
        error = "Ошибка: не задана температура"
        return render_template('lab4/fridge.html', error=error, temperature=None)

    try:
        temperature = float(temperature)
    except ValueError:
        error = "Ошибка: введите корректное число"
        return render_template('lab4/fridge.html', error=error, temperature=None)

    if temperature < -12:
        error = "Не удалось установить температуру — слишком низкое значение"
        return render_template('lab4/fridge.html', error=error, temperature=None)

    if temperature > -1:
        error = "Не удалось установить температуру — слишком высокое значение"
        return render_template('lab4/fridge.html', error=error, temperature=None)

    return render_template('lab4/fridge.html', temperature=temperature)

@lab4.route('/lab4/grain_order', methods=['GET', 'POST'])
def grain_order():
    if request.method == 'GET':
        return render_template('lab4/grain_order.html')

    grain = request.form.get('grain')
    weight = request.form.get('weight')

    if not weight:
        error = "Ошибка: не указан вес"
        return render_template('lab4/grain_order.html', error=error)

    try:
        weight = float(weight)
    except ValueError:
        error = "Ошибка: введите корректный вес"
        return render_template('lab4/grain_order.html', error=error)

    if weight <= 0:
        error = "Ошибка: вес должен быть больше 0"
        return render_template('lab4/grain_order.html', error=error)

    if weight > 500:
        error = "Ошибка: такого объёма сейчас нет в наличии"
        return render_template('lab4/grain_order.html', error=error)

    prices = {
        'ячмень': 12345,
        'овёс': 8522,
        'пшеница': 8722,
        'рожь': 14111
    }

    total_price = prices[grain] * weight

    discount = 0
    if weight > 50:
        discount = 10
        total_price *= 0.9

    order_message = f"Заказ успешно сформирован. Вы заказали {grain}. Вес: {weight} т. Сумма к оплате: {total_price} руб."
    return render_template('lab4/grain_order.html', order_message=order_message, discount=discount)