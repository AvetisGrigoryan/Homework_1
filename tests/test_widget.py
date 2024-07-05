import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("string, expected", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_mask_account_card(string: str, expected: str):
    assert mask_account_card(string) == expected


@pytest.mark.parametrize("string, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2019-08-12T02:25:19.671408", "12.08.2019"),
    ("2020-09-10T02:26:18.671407", "10.09.2020"),
    ("2021-10-11B0:27:19.199221", "21.10.2021"),
    ("2021-12-11A0:27:19.199221", "21.12.2021")
])
def test_get_date(string: str, expected: str):
    assert get_date(string) == expected
