run = float(input('Введите результат пробежки первого дня в км: -'))
target = float(input('Введите желаемый результат в км: -'))
day = 1


while run <= target:
    run = run + (run * 0.1)
    day += 1

print(f"Цель будет достигнута на {day} день")

