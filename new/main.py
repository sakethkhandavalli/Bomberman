'''This file has the main code for working of the game'''
from select import select
import os
import time
import random
import tty
import termios
import sys
from colorama import Fore
from Wall import Wall
from Person import Person
from Board import Board
from Bman import Bman
from Brick import Brick
from Enemy import Enemy
from Bomb import Bomb

def getchar():
    '''This method is used to get the input character'''
    matfd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(matfd)
    match = ''
    try:
        tty.setraw(sys.stdin.fileno())
        #[inp, out, exp] = select([sys.stdin.fileno()], [], [], 0.8)
        if not select([sys.stdin.fileno()], [], [], 0.8)[0]:
            match = None
        else:
            match = sys.stdin.read(1)
    finally:
        termios.tcsetattr(matfd, termios.TCSADRAIN, old_settings)
    # To convert case of given character
    if match is not None:
        match = match.lower()
    return match

def enmove(enlist, brd):
    '''This method is used to implement the motion of enemy'''
    matll = []
    flg = 0
    for lst in enlist:
        matl = []
        posx = lst[0]
        posy = lst[1]
        tmp1 = Wall('X').matrix
        tmp2 = Brick().matrix
        tmp3 = Enemy().matrix
        tmp4 = Bman().matrix
        tmp6 = Wall('O').matrix

        matt = brd.matrix[posx+1][posy]
        if matt != tmp1 and matt != tmp2 and matt != tmp3 and matt != tmp6:
            if matt == tmp4:
                brd.print_board()
                flg = 1
                break
            matl.append([posx+1, posy])
        matt = brd.matrix[posx-1][posy]
        if matt != tmp1 and matt != tmp2 and matt != tmp3 and matt != tmp6:
            if matt == tmp4:
                brd.print_board()
                flg = 1
                break
            matl.append([posx-1, posy])
        matt = brd.matrix[posx][posy-1]
        if matt != tmp1 and matt != tmp2 and matt != tmp3 and matt != tmp6:
            if matt == tmp4:
                brd.print_board()
                flg = 1
                break
            matl.append([posx, posy-1])
        matt = brd.matrix[posx][posy+1]
        if matt != tmp1 and matt != tmp2 and matt != tmp3 and matt != tmp6:
            if matt == tmp4:
                brd.print_board()
                flg = 1
                break
            matl.append([posx, posy+1])
        condi = len(matl)
        if condi == 0:
            matll.append([posx, posy])
        else:
            matr = random.randint(0, len(matl)-1)
            posx1 = matl[matr][0]
            posy1 = matl[matr][1]
            brd.matrix[posx][posy] = Wall(' ').matrix
            brd.matrix[posx1][posy1] = Wall('E').matrix
            matll.append([posx1, posy1])
    if flg == 1:
        return flg
    else:
        enlist = matll
    return enlist

BRD = Board()
BMAN = Bman()
TMP1 = Wall('X').matrix
TMP2 = Wall('/').matrix
TMP3 = Person('E').matrix

ENLIST = []
CNT = 0
while True:
    for i in range(len(BRD.matrix)):
        for j in range(len(BRD.matrix[i])):
            if BRD.matrix[i][j] != TMP1:
                r = random.random()
                if r <= 0.01:
                    CNT += 1
                    b = Brick()
                    BRD.matrix[i][j] = b.matrix
                if CNT > 60:
                    break
        if CNT > 60:
            break
    if CNT > 60:
        break

CNT = 0

while True:
    for i in range(len(BRD.matrix)):
        for j in range(len(BRD.matrix[i])):
            if BRD.matrix[i][j] != TMP1 and BRD.matrix[i][j] != TMP2 and i != 1 and j != 1:
                r = random.random()
                if r <= 0.01:
                    CNT += 1
                    e = Enemy()
                    BRD.matrix[i][j] = e.matrix
                    e.posx = i
                    e.posy = j
                    ENLIST.append([i, j])
                if CNT > 10:
                    break
        if CNT > 10:
            break
    if CNT > 10:
        break

BRD.matrix[1][1] = BMAN.matrix
BRD.print_board()
BCNT = 0
BFLG = 0
SCORE = 0
LIFE = 3
START = int(time.time())
BOMB = Bomb(BMAN.posx, BMAN.posy)

while LIFE > 0 and int(time.time()) - START <= 100:
    MATCH = getchar()
    FL = 0

    if BFLG == 1 and BCNT == 3:
        POSX = BOMB.explode(BRD)
        BRD = POSX[0]
        FL = POSX[1]
        if FL == 1:
            LIFE -= 1
        ENE = POSX[2]
        SC = POSX[3]
        SCORE += 20*SC
        for i in ENE:
            SCORE += 100
            ENLIST.remove([i[0], i[1]])
        BFLG = 0
        if BMAN.posx == BOMB.posx and BMAN.posy == BOMB.posy:
            BMAN.posx = 1
            BMAN.posy = 1
            BRD.matrix[1][1] = BMAN.matrix
            LIFE = LIFE - 1
            if [1, 1] in ENLIST:
                ENLIST.remove([1, 1])

    if MATCH == 'q':
        quit()

    elif MATCH == 'b':
        if BFLG == 0:
            BOMB = Bomb(BMAN.posx, BMAN.posy)
            BCNT = 0
            BFLG = 1

    elif MATCH == 'a':
        BRD = BMAN.move_left(BRD)
        if BMAN.flag == 1:
            LIFE -= 1
            FL = 1
        else:
            if BFLG == 1:
                if BCNT == 0:
                    BRD.matrix[BMAN.posx][BMAN.posy+1] = BOMB.matrix
                BCNT += 1
            YEPX = enmove(ENLIST, BRD)
            if YEPX == 1:
                LIFE -= 1
                FL = 1
            else:
                ENLIST = YEPX
    elif MATCH == 'd':
        BRD = BMAN.move_right(BRD)
        if BMAN.flag == 1:
            LIFE -= 1
            FL = 1
        else:
            if BFLG == 1:
                if BCNT == 0:
                    BRD.matrix[BMAN.posx][BMAN.posy-1] = BOMB.matrix
                BCNT += 1
            YEPX = enmove(ENLIST, BRD)
            if YEPX == 1:
                LIFE -= 1
                FL = 1
            else:
                ENLIST = YEPX
    elif MATCH == 'w':
        BRD = BMAN.move_up(BRD)
        if BMAN.flag == 1:
            LIFE -= 1
            FL = 1
        else:
            if BFLG == 1:
                if BCNT == 0:
                    BRD.matrix[BMAN.posx+1][BMAN.posy] = BOMB.matrix
                BCNT += 1
            YEPX = enmove(ENLIST, BRD)
            if YEPX == 1:
                LIFE -= 1
                FL = 1
            else:
                ENLIST = YEPX
    elif MATCH == 's':
        BRD = BMAN.move_down(BRD)
        if BMAN.flag == 1:
            LIFE -= 1
            FL = 1
        else:
            if BFLG == 1:
                if BCNT == 0:
                    BRD.matrix[BMAN.posx-1][BMAN.posy] = BOMB.matrix
                BCNT += 1
            YEPX = enmove(ENLIST, BRD)
            if YEPX == 1:
                LIFE -= 1
                FL = 1
            else:
                ENLIST = YEPX

    elif MATCH is None:
        if BFLG == 1:
            BCNT += 1
        YEPX = enmove(ENLIST, BRD)
        print(YEPX)
        if YEPX == 1:
            LIFE -= 1
            FL = 1
        else:
            ENLIST = YEPX

    else:
        pass

    if FL == 1:
        BRD.matrix[BMAN.posx][BMAN.posy] = Wall(' ').matrix
        BRD.matrix[1][1] = BMAN.matrix
        BMAN.posx = 1
        BMAN.posy = 1
        if [1, 1] in ENLIST:
            ENLIST.remove([1, 1])
    os.system('clear')
    BRD.print_board()

    print('Score is : ', SCORE)
    if FL == 1:
        print('Lives : ', LIFE, ' One life decreased')
    else:
        print('Lives : ', LIFE)
    if 100-(int(time.time()) - START) < 0:
        print('Time Left : ', 0)
    else:
        print('Time Left : ', 100-(int(time.time())-START))
    LEN = len(ENLIST)
    if LEN == 0:
        break
LEN = len(ENLIST)
if LEN == 0:
    print(Fore.CYAN + '\033[1m' + 'You have won the Game')
elif LIFE == 0:
    print(Fore.RED + '\033[1m' + 'Game over')
else:
    print(Fore.RED + '\033[1m' + 'Time is up')
