weight,height=map(float,input('Введите ваш вес (в кг) и рост (в метрах): ').split())
imt=weight/height**2
print(f'Ваш ИМТ: {imt:.1f}')