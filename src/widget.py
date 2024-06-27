from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account_number: str) -> str | None:
    """ Функция, которая маскирует номер карты и счета """

    if "Счет" in card_or_account_number:
        account_disguise = f"Счет {get_mask_account(card_or_account_number[-20:])}"
        return account_disguise
    else:
        card_number = get_mask_card_number(card_or_account_number[-16:])
        masking_cards = card_or_account_number.replace(card_or_account_number[-16:], card_number)
        return masking_cards


def get_date(input_string: str) -> str | None:
    """ Функция, возвращает дату. """

    receiving_date = input_string.split("T")[0]
    format_date = f"{receiving_date[-2:]}.{receiving_date[5:7]}.{receiving_date[:4]}"
    return format_date


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(get_date("2018-07-11T02:26:18.671407"))
