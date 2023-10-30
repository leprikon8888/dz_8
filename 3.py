'''Task 3
Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. Якщо такий елемент у списку є, то \
поверніть індекс, якщо ні, то поверніть число «-1».'''
def my_func(element:int, my_list:list):
    if element not in my_list:
        return -1
    else:
        return my_list.index(element)

