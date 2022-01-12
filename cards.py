from pyglet.graphics import *
import math
class Cylinder:
    def __init__(self, radius, height, frontColor, edgeColor):
        self.radius = radius
        self.height = height

        triangles = 100
        circle = math.pi * 2
        delta = circle/triangles
        addon = 0
        #vertexes
        top = [0.0, 0.0, 0.0]
        bottom = [0.0, 0.0, height]
        edges = []
        while (addon < circle):
            #podstawa gorna
            top.append(math.sin(addon) * self.radius)
            top.append(math.cos(addon) * self.radius)
            top.append(0.0)

            #podstawa dolna
            bottom.append(math.sin(addon) * self.radius)
            bottom.append(math.cos(addon) * self.radius)
            bottom.append(height)
            
            #bok
            edges.append(math.sin(addon) * self.radius)
            edges.append(math.cos(addon) * self.radius)
            edges.append(0)
            edges.append(math.sin(addon) * self.radius)
            edges.append(math.cos(addon) * self.radius)
            edges.append(height)

            addon += delta
        #podstawa gorna
        top.append(math.sin(addon) * self.radius)
        top.append(math.cos(addon) * self.radius)
        top.append(0)

        #podstawa dolna
        bottom.append(math.sin(addon) * self.radius)
        bottom.append(math.cos(addon) * self.radius)
        bottom.append(height)
            
        #bok
        edges.append(math.sin(addon) * self.radius)
        edges.append(math.cos(addon) * self.radius)
        edges.append(0)
        edges.append(math.sin(addon) * self.radius)
        edges.append(math.cos(addon) * self.radius)
        edges.append(height)

        frontColor *= len(top) // 3
        edgeColor *= len(edges) // 3
        self.top = vertex_list(len(top)//3, ('v3f', top), ('c3f', frontColor))
        self.bottom = vertex_list(len(bottom)//3, ('v3f', bottom), ('c3f', frontColor))
        self.edges = vertex_list(len(edges)//3, ('v3f', edges), ('c3f', edgeColor))
    def draw(self):
        self.top.draw(GL_TRIANGLE_FAN)
        self.bottom.draw(GL_TRIANGLE_FAN)
        self.edges.draw(GL_QUAD_STRIP)
class Card:
    def CreateEdges(self, front, edge):
        front *= 4
        edge *= 4
        z = [0.0, self.depth]
        for zi in z:
            vertex = [-self.width/2, -self.height/2+self.radius, zi,
                    -self.width/2, self.height/2-self.radius, zi,
                    -self.width/2+2*self.radius, self.height/2-self.radius, zi,
                    -self.width/2+2*self.radius, -self.height/2+self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-self.width/2+self.radius, self.height/2-2*self.radius, zi,
                    -self.width/2+self.radius, self.height/2, zi,
                    self.width/2-self.radius, self.height/2, zi,
                    self.width/2-self.radius, self.height/2-2*self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [self.width/2-2*self.radius, self.height/2-self.radius, zi,
                    self.width/2, self.height/2-self.radius, zi,
                    self.width/2, -self.height/2+self.radius, zi,
                    self.width/2-2*self.radius, -self.height/2+self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-self.width/2+self.radius, -self.height/2+2*self.radius, zi,
                    self.width/2-self.radius, -self.height/2+2*self.radius, zi,
                    self.width/2-self.radius, -self.height/2, zi,
                    -self.width/2+self.radius, -self.height/2, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-self.width/2, -self.height/2+self.radius, zi,
                    -self.width/2, self.height/2-self.radius, zi,
                    -self.width/2+2*self.radius, self.height/2-self.radius, zi,
                    -self.width/2+2*self.radius, -self.height/2+self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-self.width/2+self.radius, self.height/2-2*self.radius, zi,
                    -self.width/2+self.radius, self.height/2, zi,
                    self.width/2-self.radius, self.height/2, zi,
                    self.width/2-self.radius, self.height/2-2*self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [self.width/2-2*self.radius, self.height/2-self.radius, zi,
                    self.width/2, self.height/2-self.radius, zi,
                    self.width/2, -self.height/2+self.radius, zi,
                    self.width/2-2*self.radius, -self.height/2+self.radius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-self.width/2+self.radius, -self.height/2+2*self.radius, zi,
                    self.width/2-self.radius, -self.height/2+2*self.radius, zi,
                    self.width/2-self.radius, -self.height/2, zi,
                    -self.width/2+self.radius, -self.height/2, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
    def DrawCylinders(self):
        glPushMatrix()
        glTranslatef(-self.width/2+self.radius, -self.height/2+self.radius, 0.0)
        self.cylinder.draw()
        glTranslatef(0.0, self.height-2*self.radius, 0.0)
        self.cylinder.draw()
        glTranslatef(self.width-2*self.radius, 0.0, 0.0)
        self.cylinder.draw()
        glTranslatef(0.0, -self.height+2*self.radius, 0.0)
        self.cylinder.draw()
        glPopMatrix()
    def createField(self, depth):
        vertex = [-self.width/2+self.radius, -self.height/2+self.radius, depth,
                -self.width/2+self.radius, self.height/2-self.radius, depth,
                self.width/2-self.radius, self.height/2-self.radius, depth,
                self.width/2-self.radius, -self.height/2+self.radius, depth]
        color = [1.0, 0.0, 0.0] * 4
        return vertex_list(4, ('v3f', vertex), ('c3f', color))
    def __init__(self, x, y, width):
        self.batch = Batch()
        self.depth = -10.0
        self.edges = Group()
        self.width = 100
        self.height = 150
        self.radius = 5
        self.rotation = 0.0

        self.x = x
        self.y = y

        #declare elements
        self.cylinder = Cylinder(self.radius, self.depth, [1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.CreateEdges([1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.front = self.createField(0.1)
        self.back = self.createField(self.depth-0.1)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glRotatef(self.rotation, 0, 1, 0)
        self.batch.draw()
        self.DrawCylinders()
        self.front.draw(GL_QUADS)
        self.back.draw(GL_QUADS)
        glPopMatrix()
class Player:
        def __init__(self, playable):
                self.playable = playable

