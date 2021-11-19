profit = int(input('Введите вашу выручку: -'))
lesion = int(input('Введите ваши издержки: -'))
f_profit = int(profit - lesion)
profitability = float((profit - lesion) / profit)

if profit > lesion:
    print(f'Фирма работает с прибылью. Рентабельность выручки составяет {profitability}')
    employees = int(input('Введите количество сотрудников: - '))
    print(f"Прибыль на сотрудника составляет {f_profit / employees}")

elif profit == lesion:
    print('Компания работает в ноль')

else:print('Компания работает в убыток')