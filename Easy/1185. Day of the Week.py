import datetime


def dayOfTheWeek(day, month, year):
    return datetime.datetime(year, month, day).strftime('%A')
