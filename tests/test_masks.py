from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_info: str) -> None:
    """Функция передает строку с номером карты"""
    assert get_mask_card_number(card_info) == '7000 79** **** 6361'


def test_mask_account(account_info: str) -> None:
    """Функция передает строку с номером счета"""
    assert get_mask_account(account_info) == '**4305'