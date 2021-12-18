from bs4 import BeautifulSoup
import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import telebot
import keyboards as kb


def weather():
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



    def get_content(html):
            global item
            soup = BeautifulSoup(html, 'html.parser')
            item = soup.find('div', class_='_1HBR').text
            #i = soup.find('span', class_='_29Kw').text
            print('1 - ', item)


    parse()




bot = telebot.TeleBot('')
controller = {}

button_1 = types.KeyboardButton('Погода сегодня')
button_2 = types.KeyboardButton('Погода завтра')
weather_kb = types.ReplyKeyboardMarkup()
weather_kb.add(button_1).add(button_2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     """               
                     Это бот, который подскажет вам погоду. Выберете что вы хотите узнать. На данный момент есть два варианта: погода на сегодня и на завтра.
                     """,  reply_markup=kb.weather_kb)
    user_id = message.from_user.id
    controller[user_id] = 'start'

def weather_bot(user_id, user_choice):
    if user_choice == "Погода сегодня":
        controller[user_id] = 'start'
        return weather()
