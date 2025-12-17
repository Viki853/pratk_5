salary=float(input("Введите Ваш доход: "))
nalog=0.13
tax=salary*nalog
total_salary=salary-tax
print(f'Коэфицент текущего налога: {nalog}')
print(f'Сумма налога от заработанной суммы: {tax:.2f}')
print(f'Ваш доход после вычесления налога равен: {total_salary:.2f}')