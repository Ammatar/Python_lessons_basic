
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:

    def __init__(self, point_a_x, point_a_y, point_b_x, point_b_y, point_c_x, point_c_y):
        self.point_a_x = point_a_x
        self.point_b_x = point_b_x
        self.point_c_x = point_c_x
        self.point_a_y = point_a_y
        self.point_b_y = point_b_y
        self.point_c_y = point_c_y

    def ploshad(self):
        self.ploshad= ((self.point_a_x - self.point_c_x)*(self.point_b_y - self.point_c_y) - (self.point_b_x - self.point_c_x)*(self.point_a_y - self.point_c_y))/2
        return abs(self.ploshad)
    def perim(self):
        a = math.sqrt((self.point_b_x - self.point_a_x) ** 2 + (self.point_b_y - self.point_a_y) ** 2)
        b = math.sqrt((self.point_c_x - self.point_a_x) ** 2 + (self.point_c_y - self.point_a_y) ** 2)
        c = math.sqrt((self.point_c_x - self.point_b_x) ** 2 + (self.point_c_y - self.point_b_y) ** 2)
        self.perim_1 = a + b +c
        return self.perim_1
    def height(self):
        pass

ttriangle = Triangle(1,5,5,7,5,2)
print('s =',ttriangle.ploshad())
print('p =',ttriangle.perim())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, point_a, point_b, point_c, point_d):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d
    def ploshad(self):
        a = math.sqrt((self.point_b[0] - self.point_a[0]) ** 2 + (self.point_b[1] - self.point_a[1]) ** 2)
        b = math.sqrt((self.point_b[0] - self.point_c[0]) ** 2 + (self.point_b[1] - self.point_c[1]) ** 2)
        c = math.sqrt((self.point_c[0] - self.point_d[0]) ** 2 + (self.point_c[1] - self.point_d[1]) ** 2)
        d = math.sqrt((self.point_d[0] - self.point_a[0]) ** 2 + (self.point_d[1] - self.point_d[1]) ** 2)
        h = math.sqrt(c**2 -((a-b)**2)/4)
        bd = (b+d)/2
        s = ((a+b)/2)*h
        return "p = " + str(a+d+b+c), "s = " + str(s), 'a to b =' + str(a), 'b to c =' + str(b), 'c to d =' + str(c),'d to a =' + str(d)

ttrapeze = Trapeze((1,3), (3,5), (6,5), (8,3))
print(ttrapeze.ploshad())



