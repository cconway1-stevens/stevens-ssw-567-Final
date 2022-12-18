"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_Triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """Test cases for triangles"""
    # define multiple sets of tests as functions with names that begin

    def test_Right_Triangle_A(self):
        """Tests positive input for a right and scalene triangle"""
        self.assertEqual(classify_Triangle(3,4,5),'Right and Scalene','3,4,5 is a Right triangle')
    def test_Right_Triangle_B(self): 
        """Tests positive input for a right & scalene triangle with different order of lengths"""
        self.assertEqual(classify_Triangle(5,3,4),'Right and Scalene','5,3,4 is a Right triangle')
    def test_Equilateral_Triangles(self):
        """Tests positive input for equilateral triangle """
        self.assertEqual(classify_Triangle(4,4,4),'Equilateral','1,1,1 should be equilateral')
    def test_Equilateral_Triangle_A(self):
        self.assertEqual(classify_Triangle(1,1,1),'Equilateral','1,1,1 should be an equilateral triangle')
    def test_Equilateral_Triangle_B(self):
        self.assertEqual(classify_Triangle(5,5,5),'Equilateral','5,5,5 should be an equilateral triangle')
    def test_Equilateral_Triangle_C(self):
        self.assertEqual(classify_Triangle(10,10,10),'Equilateral','10,10,10 should be an equilateral triangle')


    def test_Not_A_Triangle(self):
        """Tests negative input for triangle but handles correctly"""
        self.assertEqual(classify_Triangle(4,9,2), "NotATriangle")
    def test_Wrong_Type(self):
        """Tests invalid input but handles correctly"""
        self.assertEqual(classify_Triangle(1, "snow", 3), "InvalidInput")
    def test_Isosceles_Triangle(self):
        """Tests positive input for isosceles triangle"""
        self.assertEqual(classify_Triangle(20,12,12), "Isosceles", '20,12,12 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
