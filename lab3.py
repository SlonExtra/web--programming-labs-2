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


@lab3.route('/lab3/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        user = request.form.get('user')
        age = request.form.get('age')
        sex = request.form.get('sex')

        #Преобразование пола на русский язык
        sex_ru = 'Мужской' if sex == 'male' else 'Женский'

        return render_template('lab3/form1.html', user=user, age=age, sex_ru=sex_ru)

    return render_template('lab3/form1.html')


@lab3.route('/lab3/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        drink = request.form.get('drink')
        milk = 'milk' in request.form
        sugar = 'sugar' in request.form
        return render_template('lab3/pay.html', drink=drink, milk=milk, sugar=sugar)
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay', methods=['POST'])
def pay():
    drink = request.form.get('drink')
    milk = request.form.get('milk') == 'on'
    sugar = request.form.get('sugar') == 'on'
    
    price = 0
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    elif drink == 'green-tea':
        price = 70
    
    if milk:
        price += 30
    if sugar:
        price += 10
    
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success', methods=['POST'])
def success():
    price = request.form.get('price')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        color = request.form.get('color') or 'black'
        background_color = request.form.get('background_color') or 'white'
        font_size = request.form.get('font_size') or '16'
        link_color = request.form.get('link_color') or 'blue'
        
        response = make_response(redirect('/lab3/settings'))
        response.set_cookie('color', color)
        response.set_cookie('background_color', background_color)
        response.set_cookie('font_size', font_size)
        response.set_cookie('link_color', link_color)
        
        return response
    
    color = request.cookies.get('color') or 'black'
    background_color = request.cookies.get('background_color') or 'white'
    font_size = request.cookies.get('font_size') or '16'
    link_color = request.cookies.get('link_color') or 'blue'
    
    return render_template('lab3/settings.html', color=color, background_color=background_color, font_size=font_size, link_color=link_color)