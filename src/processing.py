def filter_by_state(list_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, принимающая список словарей и возвращающая новый список"""
    new_list_dicts = []
    for dicts in list_dicts:
        if dicts["state"] == state:
            new_list_dicts.append(dicts)

    return new_list_dicts


def sort_by_date(list_dicts: list, switch: bool = True) -> list:
    """Функция принимающая список словарей и сортирующая по сроку давности"""
    return sorted(list_dicts, key=lambda d: d["date"], reverse=switch)
