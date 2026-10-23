"""Задача 5. Звіт — словник лише з типів, які розуміє JSON."""
from collections import Counter

from models import DAYS
from rules import day_name
from stats import best_day, count_by_meal, revenue_by_day


def build_report(orders, errors):
    """Звіт за чеками й помилками. Ключі — рівно ці:

    "orders"      — кількість чеків (int)
    "skipped"     — кількість помилок (int)
    "revenue"     — сума чеків, round(..., 2)
    "average"     — середній чек, round(..., 2); 0.0, якщо чеків немає
    "best_day"    — день з найбільшим виторгом або None
    "by_day"      — {день: виторг, round(..., 2)} у порядку DAYS, лише дні з чеками
    "by_meal"     — {прийом їжі: кількість}, від більшого до меншого
    "first_order" — час першого чека, datetime.isoformat(), або None
    """

    revenue = revenue_by_day(orders)
    orders_check = min(order.timestamp for order in orders).isoformat() if orders else None
    average_check = round(sum(revenue.values()) / len(orders), 2) if orders else 0.0

    report = {

        "orders": len(orders),
        "skipped": len(errors),
        "revenue": round(sum(revenue.values()), 2),
        "average": average_check,
        "best_day": best_day(revenue),

        "by_day": {day: round(amount, 2) for day, amount in
                   sorted(revenue.items(), key=lambda item: DAYS.index(item[0]), reverse=False)},

        "by_meal": {time: count for time, count in
                    sorted(count_by_meal(orders).items(), key=lambda item: item[1], reverse=True)},

        "first_order": orders_check

    }

    return report
