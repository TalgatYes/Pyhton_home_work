time = int(input("Введите время в секундах: - "))

hours = time // 3600
minutes = time // 60
seconds = time - (hours * 3600 + minutes * 60)

print(f"чч:мм:сс   {hours} : {minutes} : {seconds}")
