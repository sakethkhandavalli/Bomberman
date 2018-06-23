class Person:
    x = 0
    y = 0
    char = ''
    a = []

    def __init__(self ,char):
        a = []
        self.char = char
        i = 0
        while i<2:
            b = []
            j = 0
            while j<4:
                b.append(self.char)
                j += 1
            i += 1
            a.append(b)
        self.a = a
