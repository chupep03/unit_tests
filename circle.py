import math


def area(r):
    """
    Вычисляет площадь круга.
    Аргументы:
        r (float): радиус круга
    Возвращает:
        float: площадь круга
    """                                         
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга (длину окружности).
    Аргументы:
        r (float): радиус круга
    Возвращает:
        float: периметр круга
    """
    return 2 * math.pi * r

