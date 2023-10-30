'''Task 6
Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
Наприклад: XXII -> 22'''

РЕШЕНИЕ НЕ МОЕ, у самого не хватило извилин прийти к такому

def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal = 0
    prev_value = 0

    for symbol in reversed(roman):
        value = roman_numerals[symbol]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    return decimal


# Пример использования:
roman_numeral = input('Введите римское число: ')
decimal_value = roman_to_decimal(roman_numeral)
print(f"Десятичное представление: {decimal_value}")
