'''This file has the code for the functionalities of the Bomberman'''

from Person import Person
from Wall import Wall
from Brick import Brick
from Enemy import Enemy

class Bman(Person):
    '''This class has methods and atrributes of the Bomberman'''
    flag = 0

    def __init__(self):
        '''This method initiates the position of the Bomberman and sets the flag to 0'''
        super(Bman, self).__init__('B')
        self.posx = 1
        self.posy = 1
        self.matrix = Person('B').matrix
        self.char = 'B'
        self.flag = 0

    def move_up(self, brd):
        '''This method has the functionality for moving up'''
        tmp1 = Wall('X').matrix
        tmp2 = Brick().matrix
        tmp3 = Enemy().matrix
        tmp4 = Wall('O').matrix

        temp = brd.matrix[self.posx-1][self.posy]
        if temp == tmp3:
            self.flag = 1
        elif temp != tmp1 and temp != tmp2 and temp != tmp4:
            brd.matrix[self.posx][self.posy] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
            brd.matrix[self.posx-1][self.posy] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
            self.posx -= 1
        else:
            pass
        return brd

    def move_down(self, brd):
        '''This method has the functionality for moving down'''
        tmp1 = Wall('X').matrix
        tmp2 = Brick().matrix
        tmp3 = Enemy().matrix
        tmp4 = Wall('O').matrix

        temp = brd.matrix[self.posx+1][self.posy]
        if temp == tmp3:
            self.flag = 1
        elif temp != tmp1 and temp != tmp2 and temp != tmp4:
            brd.matrix[self.posx][self.posy] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
            brd.matrix[self.posx+1][self.posy] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
            self.posx += 1
        else:
            pass
        return brd

    def move_left(self, brd):
        '''This method has the functionality for moving left'''
        tmp1 = Wall('X').matrix
        tmp2 = Brick().matrix
        tmp3 = Enemy().matrix
        tmp4 = Wall('O').matrix

        temp = brd.matrix[self.posx][self.posy -1]
        if temp == tmp3:
            self.flag = 1
        elif temp != tmp1 and temp != tmp2 and temp != tmp4:
            brd.matrix[self.posx][self.posy] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
            brd.matrix[self.posx][self.posy-1] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
            self.posy -= 1
        else:
            pass
        return brd

    def move_right(self, brd):
        '''This method has the functionality for moving right'''
        tmp1 = Wall('X').matrix
        tmp2 = Brick().matrix
        tmp3 = Enemy().matrix
        tmp4 = Wall('O').matrix

        temp = brd.matrix[self.posx][self.posy+1]
        if temp == tmp3:
            self.flag = 1
        elif temp != tmp1 and temp != tmp2 and temp != tmp4:
            brd.matrix[self.posx][self.posy] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
            brd.matrix[self.posx][self.posy+1] = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
            self.posy += 1
        else:
            pass
        return brd
