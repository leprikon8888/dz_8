'''Task 2
Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». Її параметрами будуть цілі числа, які описують \
довжину та ширину такого прямокутника.'''
def my_func(width:int,  height:int):
    print(f"{'*' * width}\n" + f"*{' ' * (width - 2)}*\n" * (height - 2) + f"{'*' * width}\n")

my_func(4,7)