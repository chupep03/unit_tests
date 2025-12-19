import math
import unittest
#from rectangle import area as rect_area, perimeter as rect_perimeter
#from square import area as square_area, perimeter as square_perimeter
#from circle import area as circle_area, perimeter as circle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
class TriangleTests(unittest.TestCase):
    def test_positive_good_perimeter(self):
        res = triangle_perimeter(10, 20, 15)
        self.assertEqual(res, 45)
    def test_positive_good_area(self):
        res = triangle_area(20, 40, 30) 
        self.assertEqual(res, (25*5*15)**0.5)
    
    def test_negative_good_perimeter(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-10, 20, 15)
    def test_negative_good_area(self):
        with self.assertRaises(ValueError):
            triangle_area(-10, 20, 15)
    
    def test_positive_bad_perimeter(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(10, 20, 40) 
    def test_negative_bad_perimeter(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(10, 20, -40)
        
    

    


    
    
        
        
