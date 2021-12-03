def my_pow_fun(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y>= 0:
            return 'Ошибка х должен быть больше 0, а у меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1/x
            return f'результат возведения x в степени y: {round(result, 6)}'
    except ValueError:
        return "Программа работает только с числами "

print(my_pow_fun(2, -3))