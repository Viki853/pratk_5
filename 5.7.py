distance=float(input('Введите расстояние (в км): '))
rate=float(input('Введите расход топлива на 100 км: '))
price=float(input('Введите стоимость нужного топлива за литр: '))

rate_total=distance*(rate/100)
price_total=rate_total*price

print(f'Небходимое количество литров топлива на путь: {rate_total:.2f}')
print(f'Стоимость топлива на путь: {price_total:.2f}')