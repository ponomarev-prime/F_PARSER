import sqlite3

# Устанавливаем соединение с БД
conn = sqlite3.connect('news.db')
cursor = conn.cursor()

# Удаляем все записи из таблицы Google_News
cursor.execute('DELETE FROM Google_News;')
conn.commit()

# Закрываем соединение с БД
conn.close()
