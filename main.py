from bs4 import BeautifulSoup
import requests



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


URL = 'https://weather.rambler.ru/v-novosibirske/tomorrow/'
HEADERS = {''}
item = 0
item1 = 0


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')


for i in range(1):
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        global item
        item = soup.find('div', class_='_1HBR').text
        i = soup.find('span', class_='_29Kw').text  # как ощущается
        print('1 - ', item)


    parse()
URL = 'https://www.accuweather.com/en/ru/novosibirsk/294459/weather-forecast/294459'
for i in range(1):
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        global item1
        item1 = soup.find('div', class_='temp').text
        print('2 - ', item1)


    parse()
