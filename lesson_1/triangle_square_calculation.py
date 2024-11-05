import math

a, b, c = map(float, input().split())  # 3 4 5

if a <= 0 or b <= 0 or c <= 0:
    print('Стороны треугольника <= нуля. Пожалуйста, введите другие значения.')
elif (
    a + b <= c
    or b + c <= a
    or a + c <= b
):
    print('Такого треугольника не существует. Пожалуйста, введите другие значения.')
else:
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(S)
