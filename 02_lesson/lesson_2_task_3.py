from math import ceil


def square(a):
    return ceil(a ** 2)
    

result = square(float(input("Длина стороны квадрата: ")))
print(f'Округленная в большую сторону сумма - {result}')
