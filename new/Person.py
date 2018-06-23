'''This file has the code for the Person'''
class Person:
    '''This class has the methods and attributes of the Person'''
    char = ''
    mata = []

    def __init__(self, char):
        '''This method initializes the attributes of the Person'''
        mata = []
        self.char = char
        self.posx = 0
        self.posy = 0
        i = 0
        while i < 2:
            matb = []
            j = 0
            while j < 4:
                matb.append(self.char)
                j += 1
            i += 1
            mata.append(matb)
        self.matrix = mata

    def getx(self):
        '''Gets x'''
        return self.posx

    def gety(self):
        '''Gets y'''
        return self.posy

    @classmethod
    def getperson(cls):
        '''This gets the person'''
        print('person')

    @classmethod
    def printperson(cls):
        '''This prints the person'''
        print('that')
