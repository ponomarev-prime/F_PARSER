import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('news.db')

# Создаем курсор
cursor = conn.cursor()

# Выполняем запрос к таблице Google_News
cursor.execute("SELECT id, created_at, prefix, title, link FROM Google_News ORDER BY id DESC LIMIT 10")

# Получаем результат запроса
rows = cursor.fetchall()

# Выводим результат на экран
for row in rows:
    id, created_at, prefix, title, link = row
    print(f"{id} {created_at} :: {title} :: {prefix}{link}")
