'''This file has the code for the Enemy'''
from Person import Person

class Enemy(Person):
    '''This class has the methods and attributes of the Enemy'''

    def __init__(self):
        '''This method initializes the attributes of the Enemy'''
        super(Enemy, self).__init__('E')
        self.posx = 0
        self.posy = 0
        self.matrix = Person('E').matrix
        self.char = 'E'

    def getx(self):
        '''Gets x'''
        return self.posx

    def get_y(self):
        '''Gets y'''
        return self.posy

    @classmethod
    def getenemy(cls):
        '''This gets the enemy'''
        print('enemy')

    @classmethod
    def printenemy(cls):
        '''This prints the enemy'''
        print('they')
