def calculate():
    while True:
        try:
            print("Калькулятор. Введите два операнда и один оператор (+, -, /, *), или 'quit' для выхода:")
            s = input().strip()

            if s.lower() == 'quit':
                print("Программа завершена.")
                break

            parts = s.split()
            if len(parts) != 3:
                raise ValueError("Неверный формат ввода. Пример: 2 + 3")

            a_str, op, b_str = parts

            try:
                a = int(a_str)
                b = int(b_str)
            except ValueError:
                print("операнды должны быть целыми числами")
                continue 

            if a < 1 or a > 10 or b < 1 or b > 10:
                print("Числа должны быть от 1 до 10 включительно")
                continue

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a // b
            else:
                print("Неверный оператор. Допустимые: +, -, *, /")
                continue

            print(f"Результат: {result}")

        except Exception as e:
            print(f"Ошибка: {e}")


calculate()
