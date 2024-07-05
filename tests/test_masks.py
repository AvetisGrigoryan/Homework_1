import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("string, expected", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
])
def test_get_mask_card_number(string, expected):
    assert get_mask_card_number(string) == expected


@pytest.mark.parametrize("string, expected", [
    ("12345678901234567340", "**7340"),
    ("12345678901234567890", "**7890"),
])
def test_get_mask_account(string, expected):
    assert get_mask_account(string) == expected
