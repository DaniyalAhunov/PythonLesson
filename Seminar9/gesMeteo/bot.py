import json
import telebot
import requests as req
from geopy import geocoders
from tokensy import token, token_accu, token_yandex



def code_location(latitude: str, longitude: str, token_accu: str):
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' \
                       f'{token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']
    return code


def weather(code_loc: str, token_accu: str):
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{code_loc}?' \
                  f'apikey={token_accu}&language=ru&metric=True'
    response = req.get(url_weather, headers={"APIKey": token_accu})
    json_data = json.loads(response.text)
    dict_weather = dict()
    dict_weather['link'] = json_data[0]['MobileLink']
    time = 'сейчас'
    dict_weather[time] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range(1, len(json_data)):
        time = 'через' + str(i) + 'ч'
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    return dict_weather


def print_weather(dict_weather, message):
    bot.send_message(message.from_user.id, f'''Разрешите доложить, {message.from_user.first_name}!
\nТемпература сейчас {dict_weather["сейчас"]["temp"]}!
А на небе {dict_weather["сейчас"]["sky"]}.
\nТемпература через три часа {dict_weather["через3ч"]["temp"]}!
А на небе {dict_weather["через3ч"]["sky"]}.
\nТемпература через шесть часов {dict_weather["через6ч"]["temp"]}!
А на небе {dict_weather["через6ч"]["sky"]}.
\nТемпература через девять часов {dict_weather["через9ч"]["temp"]}!
\nА на небе {dict_weather["через9ч"]["sky"]}.''')
    bot.send_message(message.from_user.id, f' А здесь ссылка на подробности '
                                           f'{dict_weather["link"]}')


def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def add_city(message):
    try:
        latitude, longitude = geo_pos(message.text.lower().split('город ')[1])
        global cities
        cities[message.from_user.id] = message.text.lower().split('город ')[1]
        with open('PythonGB/Seminar9/gesMeteo/cities.json', 'w') as f:
            f.write(json.dumps(cities))
        return cities, 0
    except Exception as err:
        return cities, 1


bot = telebot.TeleBot(token)

with open('PythonGB/Seminar9/gesMeteo/cities.json', encoding='utf-8') as f:
    cities = json.load(f)


@bot.message_handler(command=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я погодабот, приятно познакомитсья, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cities
    if message.text.lower() == 'привет' or message.text.lower() == 'здорова':
        bot.send_message(message.from_user.id,
                         f' {message.from_user.first_name}! Позвольте Я доложу '
                         f' Вам о погоде! Напишите  слово "погода" и я напишу погоду в Вашем'
                         f' "стандартном" городе или напишите название города в готором Вы сейчас')
    elif message.text.lower() == 'погода':
        if message.from_user.id in cities.keys():
            city = cities[message.from_user.id]
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Твой город {city}')
            latitude, longitude = geo_pos(city)
            code_loc = code_location(latitude, longitude, token_accu)
            you_weather = weather(code_loc, token_accu)
            print_weather(you_weather, message)
        else:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Я не знаю Ваш город! Просто напиши:'
                                                   f'"Мой город *****" и я запомню твой стандартный город!')
    elif message.text.lower()[:9] == 'мой город':
        cities, flag = add_city(message)
        if flag == 0:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}!'
                                                   f' Теперь я знаю Ваш город! это'
                                                   f' {cities[message.from_user.id]}')
        else:
            bot.send_message(message.from_user.id, f' {message.from_user.first_name}!'
                                                   f' Что то пошло не так :(')
    else:
        try:
            city = message.text
            bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}! Твой город {city}')
            latitude, longitude = geo_pos(city)
            code_loc = code_location(latitude, longitude, token_accu)
            you_weather = weather(code_loc, token_accu)
            print_weather(you_weather, message)
            # yandex_weather_x = yandex_weather(latitude, longitude, token_yandex)
            # print_yandex_weather(yandex_weather_x, message)
        except AttributeError as err:
            bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Не вели казнить,'
                                                   f' вели слово молвить! Я не нашел такого города!'
                                                   f'И получил ошибку {err}, попробуй другой город')


bot.polling(none_stop=True)
