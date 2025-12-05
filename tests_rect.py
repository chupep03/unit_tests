import math
import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
#from square import area as square_area, perimeter as square_perimeter
#from circle import area as circle_area, perimeter as circle_perimeter

class RectangleTests(unittest.TestCase):
    def test_two_positive_sides_area(self):
        res = rect_area(10, 10)
        self.assertEqual(res, 100)
    def test_one_zero_side_area(self):
        res = rect_area(10, 0)
        self.assertEqual(res, 0)
    def test_two_zero_sides_area(self):
        res = rect_area(0 , 0)
        self.assertEqual(res, 0)
    def test_one_negative_side_area(self):
        with self.assertRaises(ValueError):
            rect_area(-10, 10)
    def test_two_negative_sides_area(self):
        with self.assertRaises(ValueError):
            rect_area(-10, -10)

    def test_two_positive_sides_perimeter(self):
        res = rect_perimeter(10, 20)
        self.assertEqual(res, 60)
    def test_one_zero_side_perimeter(self):
        with self.assertRaises(ValueError):
            rect_perimeter(0, 10)
    def test_two_zero_sides_perimeter(self):
        with self.assertRaises(ValueError):
            rect_perimeter(0, 0)
    def test_one_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            rect_perimeter(20, -10)
    def test_two_negative_sides_perimeter(self):
        with self.assertRaises(ValueError):
            rect_perimeter(-20, -10)
    


    
    
        
        
