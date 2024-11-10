while True:
    decimal_input = input("Введите десятичное число")
    
    if decimal_input.isdigit() and int(decimal_input) >= 0:
        decimal_number = int(decimal_input)
        break
    else:
        print("Ошибка: введено некорректное число. Пожалуйста, введите положительное целое число.")
