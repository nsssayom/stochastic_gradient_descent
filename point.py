from random import randrange


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = randrange(256)
        self.g = randrange(256)
        self.b = randrange(256)
