'''This file has the code for the Bomb'''
import time
from Wall import Wall
from Person import Person

class Bomb(Wall):
    '''This class has the methods and atrributes of the bomb'''
    posx = 0
    posy = 0

    def __init__(self, posx, posy):
        '''This method initiates the attributes of the bomb'''
        super(Bomb, self).__init__('B')
        self.matrix = Wall('O').matrix
        self.posx = posx
        self.posy = posy

    @classmethod
    def getbomb(cls):
        '''This gets the bomb'''
        print('yep')

    def getx(self):
        '''Returns posx'''
        return self.posx

    def gety(self):
        '''returns posy'''
        return self.posy

    def explode(self, brd):
        '''This method is for the explosion functionality'''
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


        mat = brd.matrix[self.posx-1][self.posy]
        if mat != tmp:
            if mat == matbm:
                flag = 1
            if mat == enemy:
                maten.append([self.posx-1, self.posy])
            if mat == matbr:
                matbs += 1
            matl.append([self.posx-1, self.posy])
        mat = brd.matrix[self.posx+1][self.posy]
        if mat != tmp:
            if mat == matbm:
                flag = 1
            if mat == enemy:
                maten.append([self.posx+1, self.posy])
            if mat == matbr:
                matbs += 1
            matl.append([self.posx+1, self.posy])
        mat = brd.matrix[self.posx][self.posy-1]
        if mat != tmp:
            if mat == matbm:
                flag = 1
            if mat == enemy:
                maten.append([self.posx, self.posy-1])
            if mat == matbr:
                matbs += 1
            matl.append([self.posx, self.posy-1])
        mat = brd.matrix[self.posx][self.posy+1]
        if mat != tmp:
            if mat == matbm:
                flag = 1
            if mat == enemy:
                maten.append([self.posx, self.posy+1])
            if mat == matbr:
                matbs += 1
            matl.append([self.posx, self.posy+1])
        brd.matrix[self.posx][self.posy] = Wall(' ').matrix
        for i in matl:
            brd.matrix[i[0]][i[1]] = mate
        brd.print_board()
        time.sleep(0.600)
        for i in matl:
            brd.matrix[i[0]][i[1]] = matw
        ans = []
        ans.append(brd)
        ans.append(flag)
        ans.append(maten)
        ans.append(matbs)
        return ans
