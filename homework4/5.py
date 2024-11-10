def solve(a, b, c):
    x = a * b + 4 * c
    return x

def number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите числовое значение!")
