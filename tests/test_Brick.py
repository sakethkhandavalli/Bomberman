'''Test cases for Brick'''
import sys
sys.path.append("../Bomberman")
from Wall import Wall
from Brick import Brick

def test_getmatrix():
    '''Test case for getmatrix'''
    br = Brick()
    mat = Wall('/').matrix
    assert br.matrix == mat
