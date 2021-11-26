user_list = input('Введимте числа через пробел:').split()

print(f'изночальный варинат {user_list}')
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(f'конечный варинат {user_list}')

