def filter_by_state(list_dicts: list, state="EXECUTED") -> list:
    """Функция, принимающая список словарей и возвращающая новый список"""
    new_list_dicts = []
    for words in list_dicts:
        for key, value in words.items():
            if value == state:
                new_list_dicts.append(words)

    return new_list_dicts


