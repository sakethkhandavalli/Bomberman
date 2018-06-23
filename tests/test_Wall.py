'''Test cases for Wall'''
import sys
sys.path.append("../Bomberman")
from Wall import Wall

def test_getmatrix():
    '''Test case for getmatrix'''
    br = Wall('X')
    mat = Wall('X').matrix
    assert br.matrix == mat
