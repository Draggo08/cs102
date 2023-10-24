import math


# Функция calculate принимает два числа (a и b) и операцию (operation),
# и возвращает результат выполнения этой операции.
def calculate(a, b, operation):
    if operation == '+':
        return a + b  # Сложение
    if operation == '*':
        return a * b  # Умножение
    if operation == '-':
        return a - b  # Вычитание
    if operation == '/':
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на нуль.")
        return a / b  # Деление
    raise ValueError("Неправильная операция")


# Функция calculator предоставляет пользователю интерфейс для ввода операции и чисел,
# а затем вызывает функцию calculate для выполнения операции.
def calculator():
    operation = input('Выбор операции:\n'
                      'Введите + , - , * , /\n'
                      'Ввод:')
    if operation not in ['+', '-', '*', '/']:
        print('Неправильно введены функции')
        return None

    print(f'Вход: число-1 число-2\nВыход: число 1 {operation} число 2')
    try:
        a, b = map(float, input('Введите два числа: ').split())
    except ValueError:
        print('Неверный формат ввода.')
        return None

    try:
        result = calculate(a, b, operation)  # Вызов функции calculate
    except ZeroDivisionError as e:
        print(str(e))
        return None
    except ValueError as e:
        print(str(e))
        return None

    return result


if __name__ == "__main__":
    result = calculator()
    if result is not None:
        print(result)
