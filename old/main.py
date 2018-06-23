from colorama import Fore
from select import select
import os
import time
import random
import tty
import termios
import sys
from Wall import Wall
from Person import Person
from Board import Board
from Bman import Bman
from Brick import Brick
from Enemy import Enemy
from Bomb import Bomb

def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = ''
    try:
        tty.setraw(sys.stdin.fileno())
        [inp , out , exp] = select([sys.stdin.fileno()],[],[],0.8)
        if not inp:
            ch = None
        else:
            ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
    # To convert case of given character
    if ch is not None :
        ch = ch.lower()
    return ch

def enmove(enlist,brd):
    ll = []
    flg = 0
    print(enlist)
    for lst in enlist:
        l = []
        x = lst[0]
        y = lst[1]
        tmp1 = Wall('X').a
        tmp2 = Brick().a
        tmp3 = Enemy().a
        tmp4 = Bman().a
        tmp5 = Wall(' ').a
        tmp6 = Wall('O').a
        
        t = brd.a[x+1][y]
        if t!=tmp1 and t!=tmp2 and t!=tmp3 and t!=tmp6:
            if t == tmp4:
                brd.print_board()
                flg = 1
                break
            l.append([x+1,y])
        t = brd.a[x-1][y]
        if t!=tmp1 and t!=tmp2 and t!=tmp3 and t!=tmp6:
            if t == tmp4:
                brd.print_board()
                flg = 1
                break
            l.append([x-1,y])
        t = brd.a[x][y-1]
        if t!=tmp1 and t!=tmp2 and t!=tmp3 and t!=tmp6:
            if t == tmp4:
                brd.print_board()
                flg = 1
                break
            l.append([x,y-1])
        t = brd.a[x][y+1]
        if t!=tmp1 and t!=tmp2 and t!=tmp3 and t!=tmp6:
            if t == tmp4:
                brd.print_board()
                flg = 1
                break
            l.append([x,y+1])
        if len(l)==0 and [x,y] not in ll:
            ll.append([x,y])
        else:
            r = random.randint(0,len(l)-1)
            x1 = l[r][0]
            y1 = l[r][1]
            brd.a[x][y] = Wall(' ').a
            brd.a[x1][y1] = Wall('E').a
            ll.append([x1,y1])
    if flg==1:
        return flg
    else:
        enlist = ll
    return enlist

brd = Board()
bman = Bman()
tmp1 = Wall('X').a
tmp2 = Wall('/').a
tmp3 = Person('E').a

enlist = []
cnt = 0
while True:
    for i in range(len(brd.a)):
        for j in range(len(brd.a[i])): 
            if brd.a[i][j] != tmp1:
                r = random.random()
                if r<=0.01:
                    cnt += 1
                    b = Brick()
                    brd.a[i][j] = b.a
                if cnt>60:
                    break
        if cnt>60:
            break
    if cnt>60:
        break

cnt = 0

while True:
    for i in range(len(brd.a)):
        for j in range(len(brd.a[i])): 
            if brd.a[i][j] != tmp1 and brd.a[i][j] != tmp2 and i!=1 and j!=1:
                r = random.random()
                if r<=0.01:
                    cnt += 1
                    e = Enemy()
                    brd.a[i][j] = e.a
                    e.x = i
                    e.y = j
                    enlist.append([i,j])
                if cnt>10:
                    break
        if cnt>10:
            break
    if cnt > 10:
        break

brd.a[1][1] = bman.a
brd.print_board()
bcnt = 0
bflg = 0
score = 0
life = 3
start = int(time.time())

while life>0 and int(time.time()) - start <= 100:
    ch = getchar()
    fl = 0

    if bflg==1 and bcnt==3:
        x = bomb.explode(brd)
        brd = x[0]
        fl = x[1]
        if fl==1:
            life -= 1
        ene = x[2]
        sc = x[3]
        score += 20*sc
        for i in ene:
            score += 100
            enlist.remove([i[0],i[1]])
        bflg    = 0
        if bman.x==bomb.x and bman.y==bomb.y :
            bman.x=1
            bman.y=1
            brd.a[1][1] = bman.a
            life = life - 1
            if [1,1] in enlist:
                enlist.remove([1,1])
  
    if ch=='q':
        quit()
    elif ch=='a':
        brd = bman.move_left(brd)
        if bman.flag==1:
            life -= 1
            fl = 1
        else:
            if bflg==1:
                if bcnt==0:
                    brd.a[bman.x][bman.y+1] = bomb.a
                bcnt += 1
            x = enmove(enlist,brd)
            if x == 1:
                life -= 1
                fl = 1
            else:
                enlist = x
    elif ch=='d':
        brd = bman.move_right(brd)
        if bman.flag==1:
            life -= 1
            fl = 1
        else:
            if bflg==1:
                if bcnt==0:
                    brd.a[bman.x][bman.y-1] = bomb.a
                bcnt += 1
            x = enmove(enlist,brd)
            if x == 1:
                life -= 1
                fl = 1
            else:
                enlist = x
    elif ch=='w':
        brd = bman.move_up(brd)
        if bman.flag==1:
            life -= 1
            fl = 1
        else:
            if bflg==1:
                if bcnt==0:
                    brd.a[bman.x+1][bman.y] = bomb.a
                bcnt += 1
            x = enmove(enlist,brd)
            if x == 1:
                life -= 1
                fl = 1
            else:
                enlist = x
    elif ch=='s':
        brd = bman.move_down(brd)
        if bman.flag==1:
            life -= 1
            fl = 1
        else:
            if bflg==1:
                if bcnt==0:
                    brd.a[bman.x-1][bman.y] = bomb.a
                bcnt += 1
            x = enmove(enlist,brd)
            if x == 1:
                life -= 1
                fl = 1
            else:
                enlist = x

    elif ch=='b':
        if bflg==0:
            bomb = Bomb(bman.x,bman.y)
            bcnt = 0
            bflg = 1

    elif ch==None:
        if bflg==1:
            bcnt += 1
        x = enmove(enlist,brd)
        if x == 1:
            life -= 1
            fl = 1
        else:
            enlist = x

    else:
        pass
        
    if fl==1:
        brd.a[bman.x][bman.y] = Wall(' ').a
        brd.a[1][1] = bman.a
        bman.x = 1
        bman.y = 1
        if [1,1] in enlist:
            enlist.remove([1,1])
    os.system('clear')
    brd.print_board()

    print('Score is : ' , score)
    if fl==1:
        print('Lives : ',life , ' One life decreased')
    else:
        print('Lives : ',life)
    if 100-(int(time.time()) - start) < 0:
        print('Time Left : ' , 0)
    else:
        print('Time Left : ',100-(int(time.time())-start))
    if len(enlist)==0:
        break
if len(enlist)==0:
    print(Fore.CYAN + '\033[1m' + 'You have won the Game')
elif life==0:
    print(Fore.RED + '\033[1m' + 'Game over')
else:
    print(Fore.RED + '\033[1m' + 'Time is up')
