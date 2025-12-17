# Доступные номиналы:
B5000 = 5000
B2000 = 2000
B1000 = 1000
B500  = 500
B200  = 200
B100  = 100

# Ввод суммы
amount = int(input("Введите сумму для снятия (кратную 100): "))

# Расчёт количества купюр
n5000 = amount // B5000
amount = amount % B5000

n2000 = amount // B2000
amount = amount % B2000

n1000 = amount // B1000
amount = amount % B1000

n500 = amount // B500
amount = amount % B500

n200 = amount // B200
amount = amount % B200

n100 = amount // B100
amount = amount % B100

# Вывод результата
print("Будут выданы купюры:")
print(f'5000 - {n5000} шт.')
print(f'2000 - {n2000} шт.')
print(f'1000 - {n1000} шт.')
print(f'500 - {n500} шт.')
print(f'200 - {n200} шт.')
print(f'100 - {n100} шт.')