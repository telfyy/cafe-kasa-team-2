"""Задача 2. Розбір одного рядка каси."""
from datetime import datetime
from getpass import win_getpass

from models import RawOrder


def parse_line(line):
    """Рядок "2024-07-19 18:30;540.00;50;2" → RawOrder.
    Поля через ";": час "%Y-%m-%d %H:%M", сума, чайові, кількість гостей.
    Зіпсований рядок → ValueError з поясненням людською мовою:
    не 4 поля, не число, неіснуюча дата, сума <= 0, чайові < 0, гостей < 1.
    """

    unp_list = line.split(";")

    if len(unp_list) != 4:
        raise ValueError(f"Помилка, очікували 4 поля, а маємо {len(unp_list)}")

    try:

        date = unp_list[0]
        timestamp = datetime.strptime(date, "%Y-%m-%d %H:%M")

        total_bill = float(unp_list[1])
        tip = int(unp_list[2])
        size = int(unp_list[3])

    except ValueError as e:
        raise ValueError("Помилка, неіснуюча дата або не число")

    if total_bill <= 0 or tip < 0 or size < 1:
        raise ValueError("Зіпсований рядок, сума <= 0, чайові < 0, гостей < 1")

    return RawOrder(total_bill, tip, size, timestamp)
