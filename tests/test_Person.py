'''Test cases for Person'''
import sys
sys.path.append("../Bomberman")
from Person import Person

def test_getx():
    '''Test case for getx'''
    p = Person('B')
    assert p.getx() == 0

def test_gety():
    '''Test case for gety'''
    p = Person('B')
    assert p.gety() == 0
