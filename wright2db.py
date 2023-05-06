import sqlite3

prefix = "prefix."
news_titles = ['x1', 'x2']
news_links = ['//////', '/////']

# создать подключение
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('news.db')
        print(f'Successfully connected to SQLite version {sqlite3.version}')
    except sqlite3.Error as e:
        print(e)
    
    return conn

# Запись в БД
def insert_news(conn, prefix, title, link):
    sql = '''INSERT INTO Google_News (created_at, prefix, title, link)
             VALUES (datetime('now'),?,?,?)'''
    conn.execute(sql, (prefix, title, link))

#
def wright2db():    
    # Получаем курсор для выполнения запросов
    conn = create_connection()

    # Выводим for'ом из списков заголовок и ссылки
    for title, link in zip(news_titles, news_links):
        # Изменяем ссылку для получения полной версии
        link = link.replace('./', '/')
        link = link
        # Выводим заголовок и ссылку
        print(f"{title} :: {link}")
        # Добавляем запись в базу данных
        insert_news(conn, prefix, title, link)

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение
    conn.close()

wright2db()