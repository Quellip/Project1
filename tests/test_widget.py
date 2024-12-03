from src.widget import get_date, mask_account_card


def test_mask_account_card(mask_account_info: str) -> None:
    """Функция передает строку с номером карты или счета"""
    assert mask_account_card(mask_account_info) == "7000 79** **** 6361"


def test_get_new_data(get_data_info: str) -> None:
    """Функция передает строку с датой"""
    assert get_date(get_data_info) == "11.03.2024"
