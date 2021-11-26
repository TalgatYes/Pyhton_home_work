my_list = ['winter', 'spring', 'summer', 'autumn']
my_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите месяц по номеру "))

if month >=3 and month <6:
     print(my_dict.get(2))
elif month >=6 and month <9:
     print(my_dict.get(3))
elif month >=9 and month <12:
     print(my_dict.get(4))
else:
     print(my_dict.get(1))
