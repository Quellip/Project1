def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает зашифрованный вид карты пользователя"""
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    mask_card = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
    return mask_card


def get_mask_account(number_score: str) -> str:
    """Функция, которая  возвращает зашифрованный счёт пользователя"""
    private_account = len(number_score[-6:-4]) * "*" + number_score[-4:]
    return private_account
