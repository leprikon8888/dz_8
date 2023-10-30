'''Task 4
Напишіть функцію, яка поверне кількість слів у текстовому рядку.'''
def my_func(text:str):
    import string
    clean = ''.join(char for char in text if char not in string.punctuation)
    return len(clean.split())
print(my_func('привет, как твои дела? ! ! !'))