class Wall:
    a = []
    def __init__(self , char):
        i = 0
        a = []
        self.char = char
        while i<2:
            b = []
            j = 0
            while j<4:
                b.append(self.char)
                j += 1
            a.append(b)
            i += 1
        self.a = a
