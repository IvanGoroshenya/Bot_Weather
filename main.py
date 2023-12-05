from config import TOKEN
from pprint import pprint
import datetime
import requests

def get_weather(city, TOKEN):

    code_smile = {
        'Clear': "Ясно \U00002600",
        'Clouds' : "Облачно \U00002601",
        'Rain' : 'Дождь \U00002614',
        "Drizzle" : 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow' : 'Снег \U0001F328',
        'Mist' : 'Туман \U0001F32B'
    }


    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid={TOKEN}&units=metric')
        data = r.json()
        # pprint(data)


        weather_description = data['weather'][0]['main']
        if weather_description in code_smile:
            wd = code_smile[weather_description]
        else:
            wd = 'Погода не определена , посмотрите в окно '



        city = data['name']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f'Погода в городе - {city} - {wd}\n '
              f'Влажность - {humidity} % 💧 \n '
              f'Давление - {pressure} мм.рт.ст.\n '
              f'Макс.температура - {temp_max}°C 🔥 \n '
              f'Мин.температура - {temp_min}°C ❄ \n '
              f'Скорость ветра - {wind} м/с 🌪\n '
              f'Восход солнца - {sunrise_time} 🌞️️\n '
              f'Закат солнца - {sunset_time}   🌘️')


    except Exception as ex:
        print(ex)
        print('Проверьте написание')

def main():
    city = input('Введите город - ')
    get_weather(city, TOKEN)

