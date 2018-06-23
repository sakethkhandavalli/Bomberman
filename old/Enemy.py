from Person import Person

class Enemy(Person):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = Person('E').a
        self.char = 'E'
