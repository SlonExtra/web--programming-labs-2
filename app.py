from flask import Flask
app = Flask(__name__) 

@app.route('/')

def start():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> Руди Дмитрий Константинович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>

            </ol>
        </div>

        <footer>
            &copy; Руди Дмитрий, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
"""