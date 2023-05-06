import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
from urllib.parse import urlparse, urlunparse

in_link = 'https://news.google.com/home?hl=ru&gl=RU&ceid=RU:ru'
db = 'news.db'

# Получаем префикс из сслыки
parsed_url = urlparse(in_link)
prefix = parsed_url.scheme + '://' + parsed_url.netloc

# Выполняем GET-запрос к странице
response = requests.get(in_link)

# Парсим HTML-код страницы с помощью BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все ссылки на новости на странице
news_links = [link['href'] for link in soup.find_all('a', href=True) if '/articles/' in link['href']]

# Находим соответсвующие заголовки
news_titles = [title.text for title in soup.find_all('h4', class_='gPFEn')]

# Выводим for'ом из списков зоголово и ссылок
#for title, link in zip(news_titles, news_links):
#    print(f"{title} :: {prefix}{link.replace('./', '/')}")
#    print(' ')

# создать подключение
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(f'Successfully connected to SQLite version {sqlite3.version}')
    except sqlite3.Error as e:
        print(e)
    
    return conn

# Запись в БД
def insert_news(conn, prefix, title, link):
    sql = '''INSERT INTO Google_News (created_at, prefix, title, link)
             VALUES (datetime('now'),?,?,?)'''
    conn.execute(sql, (prefix, title, link))

# Получаем курсор для выполнения запросов
conn = create_connection()

# Выводим for'ом из списков заголовок и ссылки
for title, link in zip(news_titles, news_links):
    # Изменяем ссылку для получения полной версии
    link = link.replace('./', '/')
    link = prefix + link
    # Выводим заголовок и ссылку
    #print(f"{title} :: {link}")
    # Добавляем запись в базу данных
    insert_news(conn, prefix, title, link)

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()