import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number_str, result",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("MasterCard 7158300734726758", "7158 30** **** 6758"),
        ("Счет 35383033474447895560", "**5560"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_mask_account_card(number_str: str, result: str) -> None:
    """Функция передает строку с номером карты или счета"""
    assert mask_account_card(number_str) == result


def test_get_new_data(get_data_info: str) -> None:
    """Функция передает строку с датой"""
    assert get_date(get_data_info) == "11.03.2024"
