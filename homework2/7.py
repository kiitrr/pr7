def is_positive_integer(s):
    return s.isdigit() and int(s) > 0

while True:
    decimal_input = input("Введите десятичное число: ")
    
  
    if is_positive_integer(decimal_input):
        decimal_number = int(decimal_input)  
        break  
    else:
        print("Ошибка: введено некорректное число. Пожалуйста, введите положительное целое число.")

