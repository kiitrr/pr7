while True:
    decimal_input = input("Введите десятичное число: ")
    
    if decimal_input.isdigit() and int(decimal_input) >= 0:
        decimal_number = int(decimal_input)
        break
    else:
        print("Ошибка: введено некорректное число. Пожалуйста, введите положительное целое число.")

result = ""
if decimal_number == 0:
    result = "0"
else:
    while decimal_number > 0:
        result = str(decimal_number % 3) + result
        decimal_number //= 3

print(f"Число в троичной системе счисления: {result}")
