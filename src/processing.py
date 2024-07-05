from typing import Any

original_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(original_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """ Функция, возвращает новый список словарей по ключу 'state' """
    new_list = []
    for key in original_list:
        if key.get('state') == state:
            new_list.append(key)
    return new_list


def sort_by_date(original_list: list[dict[str, Any]], is_ascending: bool = True) -> list[dict[str, Any]]:
    """ Функция, возвращать новый список отсортированный по дате"""
    sorted_state = sorted(original_list, key=lambda original: original['date'], reverse=is_ascending)
    return sorted_state


print(filter_by_state(original_list))

print(sort_by_date(original_list))
