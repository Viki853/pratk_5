USD_TO_RUB = 95.50 #Константа

#Функция
def convert_usd_to_rub(amount_usd):
    return amount_usd * USD_TO_RUB

# Основная программа
amount_usd = float(input("Введите сумму в долларах: "))
amount_rub = convert_usd_to_rub(amount_usd)
print(f"{amount_usd:.2f} Долларов = {amount_rub:.2f} Рублей")