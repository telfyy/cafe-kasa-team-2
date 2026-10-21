"""Задача 1. Правила кафе: день тижня і прийом їжі."""
from models import DAYS


def meal_type(hour):
    """Прийом їжі за годиною: 11–15 → "обід", 17–23 → "вечеря", решта → "інше".
    # >>> meal_type(12), meal_type(16), meal_type(18)
    ('обід', 'інше', 'вечеря')
    """

    if 11 <= hour <= 15:
        time = "обід"

    elif 17 <= hour <= 23:
        time = "вечеря"

    else:
        time = "інше"

    return time

    # raise NotImplementedError("задача 1: напиши meal_type()")


def day_name(timestamp):
    """Короткий день тижня з DAYS: datetime(2024, 7, 19, 18, 30) → "пт"."""
    day = DAYS[timestamp.weekday()]
    return day
