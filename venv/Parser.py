import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/car/used/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    r = requests.get(url, headers=HEADERS, params=params)
    pagination = soup.find_all('span', class_='mhide')
    print(pagination)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='content-bar')

    cars = []

    for item in items:
        cars.append({
            'link': item.find('a', class_='address').get('href'),
            'title': item.find('a', class_='address').get('title'),
            'Price USD': item.find('span', class_='bold green size22').get_text(),
            'Price UAH': item.find('span', class_='i-block').find_next('span').get_text()
        })

    return cars


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        # cars = get_content(html.text)
    else:
        print('Error')


parse()
