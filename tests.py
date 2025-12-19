import unittest

from tests_circle import CircleTests
from tests_rect import RectangleTests
from tests_square import SquareTests
from tests_triangle import TriangleTests

suite = unittest.TestSuite()
    
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CircleTests))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RectangleTests))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SquareTests))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TriangleTests))
    
runner = unittest.TextTestRunner()
result = runner.run(suite)