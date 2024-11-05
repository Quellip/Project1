def mask_account_card(card_number: str) -> str:
    """ Функция, возвращающая зашифрованный номер карты """
    number = card_number.split()[-1]
    private_number = number[:6] + (len(number[6:-4]) * "*") + number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    mask_card = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
    return mask_card


def get_date(date: str) -> str:
    """ Функция, возвращающая дату операции """
    return f'{date[8:10]}.{date[5:7]}.{date[:4]}'


print(get_date('2024-03-11T02:26:18.671407'))

