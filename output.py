"""Задача 6. Збереження звіту в JSON і текст для людини."""
import json


def save_json(report, path):
    """Записує звіт у JSON: кирилиця як є (ensure_ascii=False), відступ 2."""

    with open(path, "w", encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def format_report(report):
    """Текст звіту з п'яти рядків, наприклад:

    Чеків: 4, пропущено рядків: 5
    Виторг: 3040.00 грн, середній чек: 760.00 грн
    Найкращий день: нд
    За днями: пт 860.00, сб 980.00, нд 1200.00
    За прийомом їжі: вечеря 3, обід 1

    Порожні значення (None, порожній словник) — символ "—".
    """

    by_day_str = ', '.join(f'{day} {amount:.2f}' for day, amount in report['by_day'].items())
    by_meal_str = ', '.join(f'{time} {amount}' for time, amount in report['by_meal'].items())

    if not report['best_day']:
        report['best_day'] = '—'

    if not by_day_str:
        by_day_str = '—'

    if not by_meal_str:
        by_meal_str = '—'

    expected = (
        f"Чеків: {report['orders']}, пропущено рядків: {report['skipped']}\n"
        f"Виторг: {report['revenue']:.2f} грн, середній чек: {report['average']:.2f} грн\n"
        f"Найкращий день: {report['best_day']}\n"
        f"За днями: {by_day_str}\n"
        f"За прийомом їжі: {by_meal_str}"
    )

    return expected
