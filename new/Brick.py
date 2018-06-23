'''This file has the code for the the bricks'''
from Wall import Wall

class Brick(Wall):
    '''This class has the methods of the brick'''
    def __init__(self):
        '''This method initializes the brick'''
        super(Brick, self).__init__('/')
        self.matrix = Wall('/').matrix

    def getmatrix(self):
        '''Get matrix'''
        return self.matrix

    @classmethod
    def getbrick(cls):
        '''This gets the brick'''
        print('yep')

    @classmethod
    def printbrick(cls):
        '''This prints the brick'''
        print('no')
