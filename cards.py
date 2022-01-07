import pyglet as pg
from addons import *
class Card:
    def drawCircle(self, x, y, edges):
        vertices = circle(self.x+x, self.y+y, self.r, edges)
        vertex = pg.graphics.vertex_list(edges, ('v3f', vertices))
        return vertex
    def drawEdge(self, x, y, width, height):
        vertices = [self.x+x, self.y+y+height, 0.0, self.x+x+width, self.y+y+height, 0.0, self.x+x+width, self.y+y, 0.0, self.x+x, self.y+y, 0.0]
        vertex = pg.graphics.vertex_list(4, ('v3f', vertices))
        return vertex
    def __init__(self, x, y, width, height, radius):
        self.r = radius
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        #vertices
        self.circle1 = self.drawCircle(self.r, height-self.r, 1000)
        self.circle2 = self.drawCircle(width-self.r, height-self.r, 1000)
        self.circle3 = self.drawCircle(width-self.r, self.r, 1000)
        self.circle4 = self.drawCircle(self.r, self.r, 1000)

        #edges
        self.edge1 = self.drawEdge(self.r, height-2*self.r, width-2*self.r, 2*self.r)
        self.edge2 = self.drawEdge(width+-2*self.r, self.r, 2*self.r, height-2*self.r)
        self.edge3 = self.drawEdge(self.r, 0.0, width-2*self.r, 2*self.r)
        self.edge4 = self.drawEdge(0, self.r, 2*self.r, height-2*self.r)

        #middle
        self.middle = self.drawEdge(self.r, self.r, width-2*self.r, height-2*self.r)
    def render(self):
        self.circle1.draw(pg.gl.GL_POLYGON)
        self.circle2.draw(pg.gl.GL_POLYGON)
        self.circle3.draw(pg.gl.GL_POLYGON)
        self.circle4.draw(pg.gl.GL_POLYGON)

        self.edge1.draw(pg.gl.GL_QUADS)
        self.edge2.draw(pg.gl.GL_QUADS)
        self.edge3.draw(pg.gl.GL_QUADS)
        self.edge4.draw(pg.gl.GL_QUADS)

        self.middle.draw(pg.gl.GL_QUADS)