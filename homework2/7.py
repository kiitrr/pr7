def is_positive_integer(s):
    return s.isdigit() and int(s) > 0

while True:
    decimal_input = input("Введите десятичное число: ")
    
  
    if is_positive_integer(decimal_input):
        decimal_number = int(decimal_input)  
        break  
    else:
        print("Ошибка: введено некорректное число. Пожалуйста, введите положительное целое число.")


binary_number = bin(decimal_number)[2:] 


octal_number = oct(decimal_number)[2:]  


print(f"Число {decimal_number} в двоичной системе: {binary_number}")
print(f"Число {decimal_number} в восьмеричной системе: {octal_number}")
