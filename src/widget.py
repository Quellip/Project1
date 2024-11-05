def mask_account_card(card_name: str) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    card_number = card_name.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    mask_card = " ".join([private_number[i : i + chunk_size] for i in range(0, chunks, chunk_size)])
    return mask_card


def get_date(date: str) -> str:
    """Функция, возвращающая дату операции"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
