import unittest
from calculator import calculate  # Импортируем функцию calculate из модуля main

# Определение класса TestCalculator, наследующегося от unittest.TestCase.
class TestCalculator(unittest.TestCase):

    # Тест проверяет операцию сложения (+).
    def test_addition(self):
        result = calculate(3, 4, '+')  # Вызываем calculate с операцией сложения
        self.assertEqual(result, 7)  # Проверяем, что результат равен 7

    # Тест проверяет операцию вычитания (-).
    def test_subtraction(self):
        result = calculate(5, 2, '-')  # Вызываем calculate с операцией вычитания
        self.assertEqual(result, 3)  # Проверяем, что результат равен 3

    # Тест проверяет операцию умножения (*).
    def test_multiplication(self):
        result = calculate(6, 8, '*')  # Вызываем calculate с операцией умножения
        self.assertEqual(result, 48)  # Проверяем, что результат равен 48

    # Тест проверяет операцию деления (/).
    def test_division(self):
        result = calculate(10, 2, '/')  # Вызываем calculate с операцией деления
        self.assertEqual(result, 5.0)  # Проверяем, что результат равен 5.0

    # Тест проверяет ситуацию деления на ноль.
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, '/')  # Вызываем calculate с попыткой деления на ноль

    # Тест проверяет случай использования неверной операции.
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(5, 3, '^')  # Вызываем calculate с неверной операцией

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты с помощью unittest
