from re import S


import pyglet as pg
from pyglet.graphics import vertex_list
class Card:
    def __init__(self, x, y):
        width = 100
        height = 150
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y
        self.x3 = x + width
        self.y3 = y - height
        self.x4 = x
        self.y4 = y - height
        self.z = 1
    def get2(self):
        return (self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)
    def get3(self):
        return (self.x1, self.y1, self.z, self.x2, self.y2, self.z, self.x3, self.y3, self.z, self.x4, self.y4, self.z)
    def move(self, x, y):
        self.x1 += x
        self.x2 += x
        self.x3 += x
        self.x4 += x
        self.y1 += y
        self.y2 += y
        self.y3 += y
        self.y4 += y
    def vertex(self):
        vertex_list = pg.graphics.vertex_list(4,
        ('v3f', self.get3())
        )
        return vertex_list