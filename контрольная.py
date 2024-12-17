number1 = input(" первое число: ")
number2 = input(" второе число: ")
print(" число:", number1)
print(" число:", number2)

message = '''Выберете операцию: + : Сложение - : Вычитание / : Деление * : Умножение Ваш выбор: '''


operation = input(message)


if operation == '+':
    print('Сложение')
elif operation == '-':
    print('Вычитание')
elif operation == '/':
    print('Деление')
elif operation == '*':
    print('Умножение')
else:
    print (' операция')


if operation == '+':
    print('Сложение')
    result = number1 + number2
elif operation == '-':
    print('Вычитание')
    result = number1 - number2
elif operation == '/':
    print('Деление')
    result = number1 / number2
elif operation == '*':
    print('Умножение')
    result = number1 * number2
else:
    print(' операция')
print("Результат:", result)