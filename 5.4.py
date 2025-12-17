import math

# Функция площади прямоугольника
def calculate_rectangle_area(width, height):
    return width * height

# Функция площади круга
def calculate_circle_area(radius):
    return math.pi * radius * radius

# Основная программа. Вычисление площади прямоугольника
width = float(input("Введите первую сторону прямоугольника: "))
height = float(input("Введите вторую сторону прямоугольника: "))
area = calculate_rectangle_area(width, height)
print(f'Площадь прямоугольника равна: {area:.1f}')

# Основная программа. Вычисление площади круга по радиусу
radius=float(input('Введите радиус круга: '))
area = calculate_circle_area(radius)
print(f'Площадь круга равна: {area:.1f}')