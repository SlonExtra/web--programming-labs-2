
from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)
 

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', "Неизвестный")
    age = request.cookies.get('age', 'неизвестен') 
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response (redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response (redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
        return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
        price=0
        drink = request.args.get('drink')
        #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffee':
             price= 120
        elif drink == 'black-tea':
             price = 80
        else:
             price=70

        #Добавка молодка удорожает напиток на 30 рублей, а сахар - на 10.
        if request.args.get('milk') == 'on':
             price += 30
        if request.args.get('sugar') == 'on':
             price += 10

        return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    # Получаем параметры из запроса
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')

    # Если параметры переданы, сохраняем их в cookies
    if color or bg_color or font_size or font_style:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_style:
            resp.set_cookie('font_style', font_style)
        return resp
    else:
        # Загружаем параметры из cookies
        color = request.cookies.get('color', '#000000')
        bg_color = request.cookies.get('bg_color', '#ffffff')
        font_size = request.cookies.get('font_size', '16')
        font_style = request.cookies.get('font_style', 'normal')

        resp = make_response(render_template('lab3/settings.html', 
                                             color=color, 
                                             bg_color=bg_color, 
                                             font_size=font_size, 
                                             font_style=font_style))
        return resp

@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    
    # Удаляем все куки
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_style')
    
    return resp



@lab3.route('/lab3/train_ticket')
def train_ticket():
    passenger_name = request.args.get('passenger_name')
    shelf_type = request.args.get('shelf_type')
    with_bedding = request.args.get('with_bedding')
    with_luggage = request.args.get('with_luggage')
    age = request.args.get('age')
    departure_point = request.args.get('departure_point')
    destination_point = request.args.get('destination_point')
    travel_date = request.args.get('travel_date')
    insurance_needed = request.args.get('insurance_needed')

    if passenger_name and shelf_type and age and departure_point and destination_point and travel_date:
        age = int(age)
        
        ticket_price = 1000 if age >= 18 else 700  

        if shelf_type in ['lower', 'lower_side']:
            ticket_price += 100
        if with_bedding == 'on':
            ticket_price += 75
        if with_luggage == 'on':
            ticket_price += 250
        if insurance_needed == 'on':
            ticket_price += 150

        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

        return render_template('lab3/ticket_confirmation.html', 
                               passenger_name=passenger_name, 
                               ticket_type=ticket_type,
                               ticket_price=ticket_price,
                               departure_point=departure_point,
                               destination_point=destination_point,
                               travel_date=travel_date)

    return render_template('lab3/train_ticket.html')



# items.py

products = [
    {"name": "iPhone 14", "price": 60599, "color": "black", "brand": "Apple"},
    {"name": "Samsung Galaxy S23", "price": 60090, "color": "white", "brand": "Samsung"},
    {"name": "Google Pixel 7", "price": 39327, "color": "green", "brand": "Google"},
    {"name": "OnePlus 11", "price": 55746, "color": "blue", "brand": "OnePlus"},
    {"name": "Xiaomi 13", "price": 47300, "color": "gray", "brand": "Xiaomi"},
    {"name": "Sony WH-1000XM5", "price": 29885, "color": "black", "brand": "Sony"},
    {"name": "Dell XPS 13", "price": 246990, "color": "silver", "brand": "Dell"},
    {"name": "MacBook Air M2", "price": 108990, "color": "gold", "brand": "Apple"},
    {"name": "Asus ROG Zephyrus", "price": 354990, "color": "black", "brand": "Asus"},
    {"name": "Kindle Paperwhite", "price": 19450, "color": "black", "brand": "Amazon"},
    {"name": "Samsung Galaxy Tab S8", "price": 51814, "color": "silver", "brand": "Samsung"},
    {"name": "Fitbit Charge 5", "price": 16490, "color": "black", "brand": "Fitbit"},
    {"name": "Logitech MX Master 3", "price": 10690, "color": "black", "brand": "Logitech"},
    {"name": "PlayStation 5", "price": 57990, "color": "white", "brand": "Sony"},
    {"name": "Xbox Series X", "price": 52917, "color": "black", "brand": "Microsoft"},
    {"name": "Apple Watch Series 8", "price": 32911, "color": "silver", "brand": "Apple"},
    {"name": "Nikon D3500", "price": 47800, "color": "black", "brand": "Nikon"},
    {"name": "Canon EOS M50", "price": 89999, "color": "black", "brand": "Canon"},
    {"name": "GoPro HERO10", "price": 28000, "color": "black", "brand": "GoPro"},
    {"name": "Bose QuietComfort 45", "price": 21990, "color": "black", "brand": "Bose"},
    {"name": "JBL Flip 6", "price": 11452, "color": "blue", "brand": "JBL"}
]

@lab3.route('/lab3/search')
def search():
    return render_template('lab3/search_form.html')

@lab3.route('/lab3/search_results')
def search_results():
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)

    filtered_products = [p for p in products if min_price <= p["price"] <= max_price]

    return render_template('lab3/search_results.html', products=filtered_products)