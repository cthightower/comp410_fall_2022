import re
# from types import NoneType


def find_us_phone_number(text) -> list:
    """Finds all occurrences of a US phone number in a text string"""
    # match a 10 digit phone number with area code
    return re.findall(r'\d{3}-\d{3}-\d{4}', text)


def find_visa_mastercard(text) -> list:
    """Finds all occurrences of a visa / mastercard number in a text string"""
    # match a 16 digit credit card number
    return re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', text)

# All American Express account numbers must start with “37” or “34”.
def find_amex(text) -> list:
    """Finds all occurrences of an amex number in a text string"""
    # match a 15 digit credit card number
    return re.findall(r'^(34|37)\d{2}-\d{6}-\d{5}', text)


def find_us_ssn(text) -> list:
    """Finds all occurrences of a US social security number in a text string"""
    # match a 9 digit social security number
    return re.findall(r'\d{3}-\d{2}-\d{4}', text)


def find_email(text) -> list:
    """Finds all occurrences of an email address in a text string"""
    # match an email address
    return re.findall(r'[\w.\-+]+@(?:[\w-]+\.){1,2}[a-zA-Z]{2,4}$', text)


def find_instagram_handle(text) -> list:
    """Finds all occurrences of an instagram handle in a text string"""
    # match an instagram handle
    return re.findall(r'(?<!\S)@[\w\d.]{1,30}', text)
