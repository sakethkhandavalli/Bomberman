from colorama import Fore
from Wall import Wall
from Person import Person

class Board:
    a = []

    def __init__(self):
        a = []
        c = []
        for i in range(0,21): 
            b = Wall('X')
            c.append(b.a)
        a.append(c)
        for j in range(1,18):
            if j%2==0:
                c = []
                for i in range(0,21):
                    if i%2==0:
                        b = Wall('X')
                        c.append(b.a)
                    else:
                        b = Wall(' ')
                        c.append(b.a)
                a.append(c)
            else:
                c = []
                b = Wall('X')
                c.append(b.a)
                for i in range(0,19):
                    b = Wall(' ')
                    c.append(b.a)
                b = Wall('X')
                c.append(b.a)
                a.append(c)
        c = []
        for i in range(0,21):
            b = Wall('X')
            c.append(b.a)
        a.append(c)
        self.a = a

    def print_board(self):
        for lst in self.a:
            v = []
            for l in lst:        
                s = ''
                s = s.join(l[0])
                v.append(s)
            s = ''
            s = s.join(v)
            for char in s:
                if char == 'X':
                    print(Fore.GREEN + '\033[1m' + 'X' , end = '')
                elif char == '/':
                    print(Fore.YELLOW + '\033[1m' + '/' , end = '')
                elif char == 'B':
                    print(Fore.BLUE + '\033[1m' + 'B' , end = '')
                elif char == 'E':
                    print(Fore.RED + '\033[1m' + 'E' , end = '')
                elif char == 'O':
                    print(Fore.MAGENTA + '\033[1m' + 'O' , end = '')
                elif char == 'e':
                    print(Fore.CYAN + '\033[1m' + 'e' , end = '')
                else:
                    print(Fore.RESET + ' ' , end = '')

            print('')
            #print(s)
            v = []
            for l in lst:        
                s = ''
                s = s.join(l[1])
                v.append(s)
            s = ''
            s = s.join(v)
            for char in s:
                if char == 'X':
                    print(Fore.GREEN + '\033[1m' + 'X' , end = '')
                elif char == '/':
                    print(Fore.YELLOW + '\033[1m' + '/' , end = '')
                elif char == 'B':
                    print(Fore.BLUE + '\033[1m' + 'B' , end = '')
                elif char == 'E':
                    print(Fore.RED + '\033[1m' + 'E' , end = '')
                elif char == 'O':
                    print(Fore.MAGENTA + '\033[1m' + 'O' , end = '')
                elif char == 'e':
                    print(Fore.CYAN + '\033[1m' + 'e' , end = '')
                else:
                    print(Fore.RESET + ' ' , end = '')
            print('')
            #print(s)
