import pytest
from calculator import osszeadas, kivonas, szorzas, osztas, gyok
def test_osszeadas():
    assert osszeadas(2, 3) == 5
    assert osszeadas(-1, 1) == 0
    assert osszeadas(0, 0) == 0
    assert osszeadas(6, 6) == 12

def test_kivonas():
    assert kivonas(5, 3) == 2
    assert kivonas(0, 0) == 0
    assert kivonas(-1, -1) == 0

def test_szorzas():
    assert szorzas(2, 3) == 6
    assert szorzas(-1, 1) == -1
    assert szorzas(0, 5) == 0

def test_osztas():
    assert osztas(6, 3) == 2
    assert osztas(-6, 2) == -3
    assert osztas(5, 0) == "Hiba: nullával való osztás!"

def test_gyok():
    assert gyok(9) == 3
    assert gyok(0) == 0
    assert gyok(-4) == "Hiba: negatív számnak nincs valós gyöke!"

#python -m pytest .\test_calculator.py -v