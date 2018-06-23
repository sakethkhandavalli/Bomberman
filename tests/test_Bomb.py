'''Test cases for Bomberman'''
import time
import sys
sys.path.append("../Bomberman")
from Wall import Wall
from Bomb import Bomb
from Board import Board
from Person import Person

def test_getx():
    '''Test case for getx'''
    bomb = Bomb(3, 3)
    assert bomb.getx() == 3

def test_gety():
    '''Test case for gety'''
    bomb = Bomb(3, 3)
    assert bomb.gety() == 3

def test_explode():
    '''Test case for explode'''
    brd = Board()
    bomb = Bomb(2,3)

    san = bomb.explode(brd)

    x = bomb.getx()
    y = bomb.gety()
    matl = []
    maten = []
    matbs = 0
    flag = 0
    tmp = Wall('X').matrix
    matbm = Person('B').matrix
    enemy = Person('E').matrix
    mate = Wall('e').matrix
    matw = Wall(' ').matrix
    matbr = Wall('/').matrix

    mat = brd.matrix[x-1][y]
    if mat != tmp:
        if mat == matbm:
            flag = 1
        if mat == enemy:
            maten.append([x-1, y])
        if mat == matbr:
            matbs += 1
        matl.append([x-1, y])
    mat = brd.matrix[x+1][y]
    if mat != tmp:
        if mat == matbm:
            flag = 1
        if mat == enemy:
            maten.append([x+1, y])
        if mat == matbr:
            matbs += 1
        matl.append([x+1, y])
    mat = brd.matrix[x][y-1]
    if mat != tmp:
        if mat == matbm:
            flag = 1
        if mat == enemy:
            maten.append([x, y-1])
        if mat == matbr:
            matbs += 1
        matl.append([x, y-1])
    mat = brd.matrix[x][y+1]
    if mat != tmp:
        if mat == matbm:
            flag = 1
        if mat == enemy:
            maten.append([x, y+1])
        if mat == matbr:
            matbs += 1
        matl.append([x, y+1])
    brd.matrix[x][y] == Wall(' ').matrix
    for i in matl:
        brd.matrix[i[0]][i[1]] == mate
    time.sleep(0.600)
    for i in matl:
        brd.matrix[i[0]][i[1]] == matw
        
    assert brd == san[0]
    assert flag == san[1]
    assert maten == san[2]
    assert matbs == san[3]
