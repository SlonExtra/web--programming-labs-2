from flask import Blueprint, render_template, redirect, request, session, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    # Проверка, если данные уже сохранены в сессии
    if 'name' in session:
        name = session['name']
        age = int(session['age'])
        gender = session['gender']
        preference = session['preference']
        specific_preference = session['specific_preference']

        # Условие для возраста (ребёнок или взрослый)
        if age < 18:
            age_group = 'ребёнок'
        else:
            age_group = 'взрослый'

        # Условие для пола1
        
        if gender == 'male':
            growth_message = "желаю, ты оставался таким же красивым, сильным, добрым и всегда добивался своего!"
        else:
            growth_message = "желаю, чтобы ты оставалась такой же умной, сильной, доброй и всегда добивалась своего!"

        # Логика для определения поздравления и изображения
        if preference == 'tasty' and specific_preference == 'sweet':
            message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — мешочек конфет!"
            image = "candies.jpg"
        elif preference == 'tasty' and specific_preference == 'hearty':
            message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — корзина с вкусной едой!"
            image = "food_basket.jpg"
        elif preference == 'festive' and specific_preference == 'tree':
            message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — ёлка, которая принесёт уют и волшебство в твой дом!"
            image = "tree.jpg"
        elif preference == 'festive' and specific_preference == 'decorations':
            message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — новогодние украшения!"
            image = "decorations.jpg"
        else:
            message = f"Поздравляю тебя, {name}, {growth_message} Желаю тебе Ы и здоровья в новом году!"
            image = "default.jpg"

        # Дополнительное сообщение в зависимости от возраста
        if age_group == 'ребёнок':
            message += " Пусть Новый год принесет тебе массу удивительных моментов и веселых приключений!"
        else:
            message += f" Пусть каждый твой день будет наполнен успехом и радостью."

        return render_template('lab9/index.html', message=message, image=image)

    # Если данных нет в сессии, показываем приветственное сообщение
    return render_template('lab9/index.html', message=None)

@lab9.route('/lab9/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        # Сохраняем имя в сессии
        session['name'] = request.form['name']
        return redirect('/lab9/age')
    return render_template('lab9/name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        # Сохраняем возраст в сессии
        session['age'] = request.form['age']
        return redirect('/lab9/gender')
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        # Сохраняем пол в сессии
        session['gender'] = request.form['gender']
        return redirect('/lab9/preferences')
    return render_template('lab9/gender.html')

@lab9.route('/lab9/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        # Сохраняем предпочтения в сессии
        session['preference'] = request.form['preference']
        return redirect('/lab9/specific_preference')
    return render_template('lab9/preferences.html')

@lab9.route('/lab9/specific_preference', methods=['GET', 'POST'])
def specific_preference():
    if request.method == 'POST':
        session['specific_preference'] = request.form['specific_preference']
        return redirect('/lab9/congratulations')
    return render_template('lab9/specific_preference.html')

@lab9.route('/lab9/congratulations')
def congratulations():
    name = session.get('name')
    age = int(session.get('age'))
    gender = session.get('gender')
    preference = session.get('preference')
    specific_preference = session.get('specific_preference')

    # Условие для возраста (ребёнок или взрослый)
    if age < 18:
        age_group = 'ребёнок'
    else:
        age_group = 'взрослый'

    # Условие для пола
    if gender == 'male':
        growth_message = "желаю, ты оставался таким же красивым, сильным, добрым и всегда добивался своего!"
    else:
        growth_message = "желаю, чтобы ты оставалась такой же умной, сильной, доброй и всегда добивалась своего!"

    # Логика для определения поздравления и изображения
    if preference == 'tasty' and specific_preference == 'sweet':
        message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — мешочек конфет!"
        image = "candies.jpg"
    elif preference == 'tasty' and specific_preference == 'hearty':
        message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — корзина с вкусной едой!"
        image = "food_basket.jpg"
    elif preference == 'festive' and specific_preference == 'tree':
        message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — ёлка, которая принесёт уют и волшебство в твой дом!"
        image = "tree.jpg"
    elif preference == 'festive' and specific_preference == 'decorations':
        message = f"Поздравляю тебя, {name}, {growth_message} Вот тебе подарок — новогодние украшения!"
        image = "decorations.jpg"
    else:
        message = f"Поздравляю тебя, {name}, {growth_message} Желаю тебе Ы и здоровья в новом году!"
        image = "default.jpg"

    # Дополнительное сообщение в зависимости от возраста
    if age_group == 'ребёнок':
        message += " Пусть Новый год принесет тебе массу удивительных моментов и веселых приключений!"
    else:
        message += f" Пусть каждый твой день будет наполнен успехом и радостью."

    return render_template('lab9/congratulations.html', message=message, image=image)

@lab9.route('/lab9/reset')
def reset():
    session.clear()
    return redirect('/lab9/')
