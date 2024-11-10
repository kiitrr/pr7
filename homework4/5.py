def solve(a, b, c):
    x = a * b + 4 * c
    return x

def number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите числовое значение!")

a = number_input("Введите значение a: ")
b = number_input("Введите значение b: ")
c = number_input("Введите значение c: ")

x = solve(a, b, c)
print(f"Решение уравнения: x = {x}")


