from flask import Blueprint, render_template, request, redirect, session

lab5 = Blueprint('lab5', __name__)

# Пример данных для статей и пользователей
articles = []
users = []

@lab5.route('/lab5')
def lab5_page():
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    for user in users:
        if user['username'] == username and user['password'] == password:
            session['username'] = username
            return redirect('/lab5')
    return render_template('lab5/login.html', error="Неверный логин или пароль")

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    username = request.form.get('username')
    password = request.form.get('password')
    for user in users:
        if user['username'] == username:
            return render_template('lab5/register.html', error="Пользователь с таким именем уже существует")
    users.append({'username': username, 'password': password})
    return redirect('/lab5/login')

@lab5.route('/lab5/list')
def list_articles():
    return render_template('lab5/list.html', articles=articles)

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create_article():
    if request.method == 'GET':
        return render_template('lab5/create.html')
    title = request.form.get('title')
    content = request.form.get('content')
    articles.append({'id': len(articles) + 1, 'title': title, 'content': content})
    return redirect('/lab5/list')

@lab5.route('/lab5/article/<int:id>')
def view_article(id):
    for article in articles:
        if article['id'] == id:
            return render_template('lab5/article.html', article=article)
    return "Статья не найдена", 404