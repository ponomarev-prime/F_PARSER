import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

in_link = 'https://news.google.com/home?hl=ru&gl=RU&ceid=RU:ru'

def parse_google_news(in_link):
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
    for title, link in zip(news_titles, news_links):
        print(f"{title} :: {prefix}{link.replace('./', '/')}")
        print(' ')
    
    return prefix, news_titles, news_links


parse_google_news(in_link)