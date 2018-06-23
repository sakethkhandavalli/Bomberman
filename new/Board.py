'''This file has the code for printing the board'''

from colorama import Fore
from Wall import Wall

class Board:
    '''This class has the methods and attributes of the Board'''
    matrix = []

    def __init__(self):
        '''This method initializes the attributes of the Board'''
        matrix = []
        matc = []
        for i in range(0, 21):
            matb = Wall('X')
            matc.append(matb.matrix)
        matrix.append(matc)
        for j in range(1, 18):
            if j%2 == 0:
                matc = []
                for i in range(0, 21):
                    if i%2 == 0:
                        matb = Wall('X')
                        matc.append(matb.matrix)
                    else:
                        matb = Wall(' ')
                        matc.append(matb.matrix)
                matrix.append(matc)
            else:
                matc = []
                matb = Wall('X')
                matc.append(matb.matrix)
                for i in range(0, 19):
                    matb = Wall(' ')
                    matc.append(matb.matrix)
                matb = Wall('X')
                matc.append(matb.matrix)
                matrix.append(matc)
        matc = []
        for i in range(0, 21):
            matb = Wall('X')
            matc.append(matb.matrix)
        matrix.append(matc)
        self.matrix = matrix

    @classmethod
    def get_board(cls):
        '''Prints th-e string board'''
        print('Board')

    def getmatrix(self):
        '''Get matrix'''
        return self.matrix

    def print_board(self):
        '''Responsible for printing the Board'''
        for lst in self.matrix:
            matv = []
            for matl in lst:
                mats = ''
                mats = mats.join(matl[0])
                matv.append(mats)
            mats = ''
            mats = mats.join(matv)
            for char in mats:
                if char == 'X':
                    print(Fore.GREEN + '\033[1m' + 'X', end='')
                elif char == '/':
                    print(Fore.YELLOW + '\033[1m' + '/', end='')
                elif char == 'B':
                    print(Fore.BLUE + '\033[1m' + 'B', end='')
                elif char == 'E':
                    print(Fore.RED + '\033[1m' + 'E', end='')
                elif char == 'O':
                    print(Fore.MAGENTA + '\033[1m' + 'O', end='')
                elif char == 'e':
                    print(Fore.CYAN + '\033[1m' + 'e', end='')
                else:
                    print(Fore.RESET + ' ', end='')

            print('')
            #print(s)
            matv = []
            for matl in lst:
                mats = ''
                mats = mats.join(matl[1])
                matv.append(mats)
            mats = ''
            mats = mats.join(matv)
            for char in mats:
                if char == 'X':
                    print(Fore.GREEN + '\033[1m' + 'X', end='')
                elif char == '/':
                    print(Fore.YELLOW + '\033[1m' + '/', end='')
                elif char == 'B':
                    print(Fore.BLUE + '\033[1m' + 'B', end='')
                elif char == 'E':
                    print(Fore.RED + '\033[1m' + 'E', end='')
                elif char == 'O':
                    print(Fore.MAGENTA + '\033[1m' + 'O', end='')
                elif char == 'e':
                    print(Fore.CYAN + '\033[1m' + 'e', end='')
                else:
                    print(Fore.RESET + ' ', end='')
            print('')
            #print(s)
