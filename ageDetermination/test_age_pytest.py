import pytest
from age import categorizeByAge

def test_child_age():
    assert categorizeByAge(5) == "Child"
    assert categorizeByAge(7) == "Child"
    assert categorizeByAge(9) == "Child"
def test_teenager_age():
    assert categorizeByAge(10) == "Teenager"
    assert categorizeByAge(15) == "Teenager"
    assert categorizeByAge(18) == "Teenager"
def test_adult_age():
    assert categorizeByAge(19) == "Adult"
    assert categorizeByAge(30) == "Adult"
    assert categorizeByAge(65) == "Adult"
def test_senior_age():
    assert categorizeByAge(66) == "Senior"
    assert categorizeByAge(80) == "Senior"
    assert categorizeByAge(120) == "Senior"
def test_invalid_age_negative():
    assert categorizeByAge(-1) == "Invalid age"
    assert categorizeByAge(-10) == "Invalid age"
    assert categorizeByAge(0) == "Invalid age"
def test_invalid_age_too_high():
    assert categorizeByAge(121) == "Invalid age: 121"
    assert categorizeByAge(150) == "Invalid age: 150"
def test_boundary_conditions():
    assert categorizeByAge(9) == "Child"
    assert categorizeByAge(10) == "Teenager"
    assert categorizeByAge(18) == "Teenager"
    assert categorizeByAge(19) == "Adult"
    assert categorizeByAge(65) == "Adult"
    assert categorizeByAge(66) == "Senior"
#python -m pytest .\test_age_pytest.py -v