'''Test cases for Bman'''
import sys
sys.path.append("../Bomberman")
from Wall import Wall
from Person import Person
from Brick import Brick
from Enemy import Enemy
from Bman import Bman
from Board import Board

def test_move_up():
    bman = Bman()
    brd = Board()
    x = bman.posx
    y = bman.posy
    mat = bman.move_up(brd)

    tmp1 = Wall('X').matrix
    tmp2 = Brick().matrix
    tmp3 = Enemy().matrix
    tmp4 = Wall('O').matrix

    temp = brd.matrix[x-1][y]
    if temp == tmp3:
        self.flag = 1
    elif temp != tmp1 and temp != tmp2 and temp != tmp4:
        brd.matrix[x][y] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        brd.matrix[x-1][y] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        x -= 1
    else:
        pass
    
    assert mat == brd

def test_move_down():
    bman = Bman()
    brd = Board()
    x = bman.posx
    y = bman.posy
    mat = bman.move_down(brd)

    tmp1 = Wall('X').matrix
    tmp2 = Brick().matrix
    tmp3 = Enemy().matrix
    tmp4 = Wall('O').matrix

    temp = brd.matrix[x+1][y]
    if temp == tmp3:
        self.flag = 1
    elif temp != tmp1 and temp != tmp2 and temp != tmp4:
        brd.matrix[x][y] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        brd.matrix[x+1][y] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        x += 1
    else:
        pass
    
    assert mat == brd

def test_move_left():
    bman = Bman()
    brd = Board()
    x = bman.posx
    y = bman.posy
    mat = bman.move_left(brd)

    tmp1 = Wall('X').matrix
    tmp2 = Brick().matrix
    tmp3 = Enemy().matrix
    tmp4 = Wall('O').matrix

    temp = brd.matrix[x][y-1]
    if temp == tmp3:
        self.flag = 1
    elif temp != tmp1 and temp != tmp2 and temp != tmp4:
        brd.matrix[x][y] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        brd.matrix[x][y-1] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        y -= 1
    else:
        pass
    
    assert mat == brd

def test_move_right():
    bman = Bman()
    brd = Board()
    x = bman.posx
    y = bman.posy
    mat = bman.move_right(brd)

    tmp1 = Wall('X').matrix
    tmp2 = Brick().matrix
    tmp3 = Enemy().matrix
    tmp4 = Wall('O').matrix

    temp = brd.matrix[x][y+1]
    if temp == tmp3:
        self.flag = 1
    elif temp != tmp1 and temp != tmp2 and temp != tmp4:
        brd.matrix[x][y] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        brd.matrix[x][y+1] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        y += 1
    else:
        pass
    
    assert mat == brd
