import re
from typing import Optional


def is_amount(amountCandidate: str) -> bool:
    """Determines if the given amount string is a valid monetary amount"""
    return re.search("^\+*\$[\d,]*\.\d\d$", amountCandidate) != None


def is_timestamp(candidate: str) -> bool:
    """Determines if the given string contains a valid timestamp"""
    return (
        re.search("[0-9]{1,2} (?:minute|hour)s{0,1} ago", candidate) != None
        or re.search("\\d{1,2}\\/\\d{1,2}\\/\\d{2}", candidate)  # relative timestamp
        != None
        or re.search(  # mm/dd/yy date stamp
            "(?i)W*(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun|Yester)day\\b[sS]*", candidate
        )
        != None
    )  # day of week including Yesterday


def amount_in_cents(amount: str) -> Optional[int]:
    """Converts a dollar amount to cents"""
    cents_str = (
        amount.replace("+", "").replace("$", "").replace(".", "").replace(",", "")
    )
    if cents_str.isnumeric():
        cents = int(cents_str)
        return cents if "+" in amount else -cents
    return None
