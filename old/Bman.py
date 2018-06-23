from Person import Person
from Wall import Wall
from Brick import Brick
from Enemy import Enemy
from Bomb import Bomb

class Bman(Person):
    flag = 0

    def __init__(self):
        self.x = 1
        self.y = 1
        self.a = Person('B').a
        self.char = 'B'
        self.flag = 0

    def move_up(self ,brd):
        tmp1 = Wall('X').a
        tmp2 = Brick().a
        tmp3 = Enemy().a
        tmp4 = Wall('O').a

        t = brd.a[self.x-1][self.y]
        if t == tmp3:
            self.flag = 1
        elif t != tmp1 and t != tmp2 and t!=tmp4:
            brd.a[self.x][self.y] = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
            brd.a[self.x-1][self.y] = [['B','B','B','B'],['B','B','B','B']]
            self.x -= 1
        else:
            pass
        return brd

    def move_down(self ,brd):
        tmp1 = Wall('X').a
        tmp2 = Brick().a
        tmp3 = Enemy().a
        tmp4 = Wall('O').a

        t = brd.a[self.x+1][self.y]
        if t == tmp3:
            self.flag = 1
        elif t != tmp1 and t != tmp2 and t!=tmp4:
            brd.a[self.x][self.y] = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
            brd.a[self.x+1][self.y] = [['B','B','B','B'],['B','B','B','B']]
            self.x += 1
        else:
            pass
        return brd

    def move_left(self ,brd):
        tmp1 = Wall('X').a
        tmp2 = Brick().a
        tmp3 = Enemy().a
        tmp4 = Wall('O').a

        t = brd.a[self.x][self.y -1]
        if t == tmp3:
            self.flag = 1
        elif t != tmp1 and t != tmp2 and t != tmp4:
            brd.a[self.x][self.y] = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
            brd.a[self.x][self.y-1] = [['B','B','B','B'],['B','B','B','B']]
            self.y -= 1
        else:
            pass
        return brd

    def move_right(self ,brd):
        tmp1 = Wall('X').a
        tmp2 = Brick().a
        tmp3 = Enemy().a
        tmp4 = Wall('O').a
        
        t = brd.a[self.x][self.y+1]
        if t == tmp3:
            self.flag = 1
        elif t != tmp1 and t != tmp2 and t!=tmp4:
            brd.a[self.x][self.y] = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
            brd.a[self.x][self.y+1] = [['B','B','B','B'],['B','B','B','B']]
            self.y += 1
        else:
            pass
        return brd
