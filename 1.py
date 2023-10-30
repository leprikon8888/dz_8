'''Task 1
Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.'''
def my_func (a:int|float, b:int|float, c:str):
    return c + str(a+b)

print(my_func(2,7.6, 'hello'))