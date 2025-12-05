import math
import unittest
#from rectangle import area as rect_area, perimeter as rect_perimeter
#from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

class CircleTests(unittest.TestCase):
    def test_area_positive_radius(self):
        res = circle_area(10)
        self.assertEqual(math.pi * 100, res)
    def test_area_negative_radius(self):
        res = circle_area(-10)
        with self.assertRaises(ValueError):
            circle_area(-10)
    
    def test_perimeter_positive_radius(self):
        res = circle_perimeter(10)
        self.assertEqual(math.pi * 10, res)
    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_perimeter(10)
  
