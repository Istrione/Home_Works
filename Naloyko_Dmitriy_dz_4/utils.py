import requests
import sys
import typing
from pyquery import PyQuery as pq
from lxml import etree
from pprint import pprint

def currency_rate(currency):
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


    def send_request():
        response = requests.get(URL, timeout=2)
        if not response.ok:
            print(f'Запрос не успешен: {response.status_code}')
            sys.exit(0)
        return response


    def extract_data(tag: str):
        res = send_request()
        main_root = pq(etree.fromstring(res.content))
        curs_val = main_root.pop()
        return curs_val.xpath(f'//Valute/{tag}/text()')

    char_code = extract_data('CharCode')
    value = extract_data('Value')
    currency_list = dict(zip(char_code, value))
    # print(currency_list)
    if currency:
        print(currency_list.get(currency))
    else:
        return None

if __name__ == '__main__':
    #Проверка
    currency_rate('RUB')
    currency_rate('USD')
    currency_rate('EUR')