import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Основная программа. Ввод координат
x1,y1=map(float, input('Введите точки x1,y1 через пробел: ').split())
x2,y2=map(float, input('Введите точки x2,y2 через пробел: ').split())
x3,y3=map(float, input('Введите точки x3,y3 через пробел: ').split())

# Стороны треугольника
a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x2, y2, x3, y3)
c = calculate_distance(x3, y3, x1, y1)

# Площадь
area = calculate_triangle_area(a, b, c)
print(f'Площадь треугольника равна: {area:.1f}')