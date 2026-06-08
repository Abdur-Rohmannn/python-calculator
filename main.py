"""
Калькулятор на Python.

Функции:
- Сложение
- Вычитание
- Умножение
- Деление

Автор: Abdur-Rohman
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:

    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    choice = input("Выберите операцию")
    
    if choice == "5":
        print("Выход из программы !")
        break
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введите числовые значения !")
        continue




    if choice == "1":
        print("Результат:", add(num1, num2))
    elif choice == "2":
        print("Результат:", sub(num1, num2))
    elif choice == "3":
        print("Результат:", mul(num1, num2))
    elif choice == "4":
        if num2 == 0:
            print("Ошибка: Деление на ноль !")
        else:
            print("Результат:", div(num1, num2))
    else:
        print("Неверный выбор !")