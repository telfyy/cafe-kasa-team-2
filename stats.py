"""Задача 4. Підрахунки за днями і прийомами їжі."""
from models import RawOrder
from rules import day_name, meal_type


def revenue_by_day(orders):
    """Виторг за днями тижня: {"пт": 860.0, ...}. Лише дні, у які були чеки."""

    revenue = {}  # виторги за днями

    for order in orders:  # беремо за конкретний день

        if order.timestamp:  # якщо в цей день був чек

            key = day_name(order.timestamp)
            revenue[key] = revenue.get(key, 0) + order.total_bill

    return revenue


def best_day(revenue):
    """День з найбільшим виторгом; для порожнього словника — None."""

    best_amount = None
    best_day_name = None

    for day, amount in revenue.items():

        if best_amount is None or best_amount < amount:
            best_amount = amount
            best_day_name = day

    return best_day_name


def count_by_meal(orders):
    """Кількість чеків за прийомом їжі: {"вечеря": 3, "обід": 1}."""

    count = {}

    for order in orders:

        if order.timestamp:
            time = meal_type(order.timestamp.hour)
            count[time] = count.get(time, 0) + 1

    return count
