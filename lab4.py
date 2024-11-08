from flask import Blueprint, render_template, request

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4')
def laba4():
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
from flask import Blueprint, render_template, request, redirect

lab4 = Blueprint('lab4', __name__)

tree_count = 0  # Инициализация счётчика деревьев

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