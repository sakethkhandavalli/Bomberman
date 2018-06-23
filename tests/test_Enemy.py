'''Test cases for Enemy'''
import sys
sys.path.append("../Bomberman")
from Person import Person
from Enemy import Enemy

def test_getx():
    '''Test case for getx'''
    e = Enemy()
    assert e.getx() == 0

def test_gety():
    '''Test case for gety'''
    e = Enemy()
    assert e.gety() == 0
