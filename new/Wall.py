'''This file has the code for the Wall'''
class Wall:
    '''This class has the atrributes of the wall'''
    matw = []
    def __init__(self, char):
        '''This method initializes the attributes of the wall'''
        self.char = char
        self.matrix = self.get_matrix()

    def get_matrix(self):
        '''Returns the 2x4 Wall matrix'''
        i = 0
        matw = []
        for i in range(2):
            matb = []
            for j in range(4):
                matb.append(self.char)
                j = j/1
            matw.append(matb)
            i = i/1
        return matw

    @classmethod
    def getwall(cls):
        '''This gets the wall'''
        print('wall')

    @classmethod
    def printwall(cls):
        '''This prints the wall'''
        print('this')
