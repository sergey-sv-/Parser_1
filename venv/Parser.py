import requests
from bs4 import BeautifulSoup

# URL = 'https://auto.ria.com/search/?category_id=0&marka_id=62&model_id=585&state%5B0%5D=0&s_yers%5B0%5D=2001&po_yers%5B0%5D=2005&price_ot=&price_do='
URL = 'https://auto.ria.com/car/renault/dokker/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count (html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='content-bar')

    cars = []
    for item in items:
        cars.append({
            'Link...': item.find('a', class_='address').get('href'),
            'Title...': item.find('a', class_='address').get('title'),
            'Price USD...': item.find('span', class_='bold green size22').get_text(),
            'Price UAH...': item.find('span', class_='i-block').find_next('span').get_text()
        })

    return cars


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars =[]
        pages_count = get_pages_count(html.text)
        for page in range (1, pages_count+1):
            print(f'Parsing page {page} from {pages_count}....')
            html = get_html(URL, params={'page':page})
            cars.extend(get_content(html.text))
            # cars = get_content(html.text)
        # print(cars) # Print list of a cars
        print(len(cars))
    else:
        print('Error')


parse()
