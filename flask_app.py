from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Создаем подключение к базе данных
    conn = sqlite3.connect('news.db')

    # Создаем курсор
    cursor = conn.cursor()

    # Выполняем запрос к таблице Google_News
    cursor.execute("SELECT id, created_at, prefix, title, link FROM Google_News ORDER BY id DESC")

    # Получаем результат запроса
    rows = cursor.fetchall()

    # Закрываем соединение с базой данных
    conn.close()

    # Передаем данные в HTML-шаблон
    return render_template('index.html', rows=rows, table_name='Google_News')

if __name__ == '__main__':
    app.run()