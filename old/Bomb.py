from Wall import Wall
import time
from Person import Person

class Bomb(Wall):
    x = 0
    y = 0

    def __init__(self , x ,y):
        self.a = Wall('O').a
        self.x = x
        self.y = y

    def explode(self, brd):
        l = []
        en = []
        bs = 0
        flag = 0
        tmp = Wall('X').a
        bm = Person('B').a
        enemy = Person('E').a
        e = Wall('e').a
        w = Wall(' ').a
        br = Wall('/').a

        t = brd.a[self.x-1][self.y]
        if t!=tmp:
            if t==bm:
                flag = 1
            if t==enemy:
                en.append([self.x-1,self.y])
            if t==br:
                bs += 1
            l.append([self.x-1,self.y])
        t = brd.a[self.x+1][self.y]
        if t!=tmp:
            if t==bm:
                flag = 1
            if t==enemy:
                en.append([self.x+1,self.y])
            if t==br:
                bs += 1
            l.append([self.x+1,self.y])
        t = brd.a[self.x][self.y-1]
        if t!=tmp:
            if t==bm:
                flag = 1
            if t==enemy:
                en.append([self.x,self.y-1])
            if t==br:
                bs += 1
            l.append([self.x,self.y-1])
        t = brd.a[self.x][self.y+1]
        if t!=tmp:
            if t==bm:
                flag = 1
            if t==enemy:
                en.append([self.x,self.y+1])
            if t==br:
                bs += 1
            l.append([self.x,self.y+1])
        brd.a[self.x][self.y] = Wall(' ').a
        for i in l:
            brd.a[i[0]][i[1]] = e
        brd.print_board()
        time.sleep(0.600)
        for i in l:
            brd.a[i[0]][i[1]] = w
        ans = []
        ans.append(brd)
        ans.append(flag)
        ans.append(en)
        ans.append(bs)
        return ans
