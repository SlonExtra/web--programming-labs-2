from flask import Blueprint, render_template, redirect, url_for, request, make_response
import time

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)

@lab3.route('/lab3/cookie', methods=['GET', 'POST'])
def cookie():
    resp = make_response(redirect('/lab3'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    response = make_response(redirect(url_for('lab3.lab')))
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('name_color')
    return response

from flask import Blueprint, render_template, request, url_for

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        user = request.form.get('user')
        age = request.form.get('age')
        sex = request.form.get('sex')

        # Преобразование пола на русский язык
        sex_ru = 'Мужской' if sex == 'male' else 'Женский'

        return render_template('lab3/form1.html', user=user, age=age, sex_ru=sex_ru)

    return render_template('lab3/form1.html')