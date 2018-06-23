'''Test cases for Board'''
import sys
sys.path.append("../Bomberman")
from Wall import Wall
from Board import Board

def test_getmatrix():
    '''Test case for getmatrix'''
    bor = Board()
    mat = bor.getmatrix()
    assert bor.matrix == mat
