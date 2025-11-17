import unittest
from age import categorizeByAge
class TestCategorizeByAge(unittest.TestCase):

    def test_child_age(self):
        self.assertEqual(categorizeByAge(5), "Child")
        self.assertEqual(categorizeByAge(7), "Child")
        self.assertEqual(categorizeByAge(9), "Child")

    def test_teenager_age(self):
        self.assertEqual(categorizeByAge(10), "Teenager")
        self.assertEqual(categorizeByAge(15), "Teenager")
        self.assertEqual(categorizeByAge(18), "Teenager")

    def test_adult_age(self):
        self.assertEqual(categorizeByAge(19), "Adult")
        self.assertEqual(categorizeByAge(30), "Adult")
        self.assertEqual(categorizeByAge(65), "Adult")

    def test_senior_age(self):
        self.assertEqual(categorizeByAge(66), "Senior")
        self.assertEqual(categorizeByAge(80), "Senior")
        self.assertEqual(categorizeByAge(120), "Senior")

    def test_invalid_age_negative(self):
        self.assertEqual(categorizeByAge(-1), "Invalid age")
        self.assertEqual(categorizeByAge(-10), "Invalid age")
        self.assertEqual(categorizeByAge(0), "Invalid age")

    def test_invalid_age_too_high(self):
        self.assertEqual(categorizeByAge(121), "Invalid age: 121")
        self.assertEqual(categorizeByAge(150), "Invalid age: 150")

    def test_boundary_conditions(self):
        self.assertEqual(categorizeByAge(9), "Child")
        self.assertEqual(categorizeByAge(10), "Teenager")
        self.assertEqual(categorizeByAge(18), "Teenager")
        self.assertEqual(categorizeByAge(19), "Adult")
        self.assertEqual(categorizeByAge(65), "Adult")
        self.assertEqual(categorizeByAge(66), "Senior")

#python -m unittest .\test_age.py -v
