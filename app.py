import telebot
import surrogates
from config import keys, TOKEN
from extensions import APIException, GetPrise


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = ('Для работы с "valtabot" необходимо вводить комманды в следущем формате:\n <имя валюты>'
            ' <в какую валюту переветсти> <колличество переводимой валюты> \n Увидеть список всех'
            'доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Для работы с "valtabot" необходимо вводить комманды в следущем формате:\n <имя валюты>'
            ' <в какую валюту переветсти> <колличество переводимой валюты> \n Увидеть список всех'
            'доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
    USD = ('💲')
    RUB = ('₽')
    EUR = ('€')
    value = (f'Доступные валюты:\n Рубль {RUB}\n Доллар{USD}\n Евро {EUR}')
    bot.reply_to(message, value)



@bot.message_handler(content_types=['text'])
def conver(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise APIException('Не правильно колличество параметров')
        base, quote, amount = value
        total_base = GetPrise.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать значение\n{e}')

    else:
        text = f'Цена {amount} {base} в {quote} - {total_base * float(amount)}'
        bot.send_message(message.chat.id, text)


bot.polling()










