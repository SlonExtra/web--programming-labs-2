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