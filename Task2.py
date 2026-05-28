import re
from typing import Callable


def generator_numbers(text: str):
    """Generate all floating-point numbers from text."""
    pattern = r'\d+(?:,\d+)?'
    
    matches = re.findall(pattern, text)
    
    for number in matches:
        yield float(number.replace(',', '.'))


def sum_profit(text: str, func: Callable):
    """Calculate sum of all numbers extracted by the given function."""
    total = 0
    
    for number in func(text):
        total += number
    
    return total


text = (
    "Загальний дохід працівника складається з частини: "
    "1000,01 як основний дохід, "
    "доповнений додатковими надходженнями 27,45 і 324,00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
