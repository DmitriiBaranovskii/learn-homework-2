"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import date,time,datetime,timedelta

def print_days():
    date_now = date.today()
    date_yesterday, date_past30 = date_now - timedelta(1),date_now - timedelta(30)
    print(f' Сегодня: {date_now}\n Вчера: {date_yesterday}\n 30 дней назад: {date_past30}')


def str_2_datetime(date_string):
    return datetime.strptime(date_string,'%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
