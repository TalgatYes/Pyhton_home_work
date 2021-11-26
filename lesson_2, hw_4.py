i = input('Введите числа через пробел').split()

for ind, el in enumerate(i, 1):
    print(f'{ind}, {el[:10]}')