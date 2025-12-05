import math
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

a = int(input())
b = int(input())

print(rect_area(a, b), rect_perimeter(a, b))

a = int(input())
print(square_area(a), square_perimeter(a))

a = int(input())
print(circle_area(a), circle_perimeter(a));
