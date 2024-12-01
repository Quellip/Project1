import masks


def mask_account_card(card_name: str) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    card_number = card_name.split()[-1]
    if card_name.split()[0] == "Счет":
        mask_card = masks.get_mask_account(card_number)
    else:
        mask_card = masks.get_mask_card_number(card_number)

    return mask_card


def get_date(date: str) -> str:
    """Функция, возвращающая дату операции"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
