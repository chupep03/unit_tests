import math
import unittest
#from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
#from circle import area as circle_area, perimeter as circle_perimeter

class SquareTests(unittest.TestCase):
    def test_positive_shapes_perimeter(self):
        res = square_perimeter(10)
        self.assertEqual(40, res)
    
    def test_negative_shapes_perimeter(self):
        with self.assertRaises(ValueError):
            square_perimeter(-10)
    
    def test_positive_shapes_area(self):
        res = square_area(10)
        self.assertEqual(100, res)
    
    def test_negative_shapes_area(self):
        with self.assertRaises(ValueError):
            square_area(-10)

  
