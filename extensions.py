import requests
import json
from config import keys

class APIException(Exception):
    pass

class GetPrise:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException('Невозможно перевести одинаковую валюту')

        try:
            tiket_base = keys[base]
        except KeyError:
            raise APIException(f'Невозможно перевести валюту {base}')

        try:
            ticket_quote = keys[quote]
        except KeyError:
            raise APIException(f'Невозможно перевести валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Значение "{amount}" должно быть числом')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={tiket_base}&tsyms={ticket_quote}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base