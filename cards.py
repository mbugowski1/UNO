from pyglet.graphics import *
from pyglet import image
import math
cardWidth = 60
cardHeight = 90
cardRadius = 3
class Cylinder:
    def __init__(self, cardRadius, cardHeight, frontColor, edgeColor):
        cardRadius = cardRadius
        cardHeight = cardHeight

        triangles = 100
        circle = math.pi * 2
        delta = circle/triangles
        addon = 0
        #vertexes
        top = [0.0, 0.0, 0.0]
        bottom = [0.0, 0.0, cardHeight]
        edges = []
        while (addon < circle):
            #podstawa gorna
            top.append(math.sin(addon) * cardRadius)
            top.append(math.cos(addon) * cardRadius)
            top.append(0.0)

            #podstawa dolna
            bottom.append(math.sin(addon) * cardRadius)
            bottom.append(math.cos(addon) * cardRadius)
            bottom.append(cardHeight)
            
            #bok
            edges.append(math.sin(addon) * cardRadius)
            edges.append(math.cos(addon) * cardRadius)
            edges.append(0)
            edges.append(math.sin(addon) * cardRadius)
            edges.append(math.cos(addon) * cardRadius)
            edges.append(cardHeight)

            addon += delta
        #podstawa gorna
        top.append(math.sin(addon) * cardRadius)
        top.append(math.cos(addon) * cardRadius)
        top.append(0)

        #podstawa dolna
        bottom.append(math.sin(addon) * cardRadius)
        bottom.append(math.cos(addon) * cardRadius)
        bottom.append(cardHeight)
            
        #bok
        edges.append(math.sin(addon) * cardRadius)
        edges.append(math.cos(addon) * cardRadius)
        edges.append(0)
        edges.append(math.sin(addon) * cardRadius)
        edges.append(math.cos(addon) * cardRadius)
        edges.append(cardHeight)

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
            vertex = [-cardWidth/2, -cardHeight/2+cardRadius, 0.0,
                    -cardWidth/2, cardHeight/2-cardRadius, 0.0,
                    -cardWidth/2+2*cardRadius, cardHeight/2-cardRadius, 0.0,
                    -cardWidth/2+2*cardRadius, -cardHeight/2+cardRadius, 0.0]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2+cardRadius, cardHeight/2-2*cardRadius, 0.0,
                    -cardWidth/2+cardRadius, cardHeight/2, 0.0,
                    cardWidth/2-cardRadius, cardHeight/2, 0.0,
                    cardWidth/2-cardRadius, cardHeight/2-2*cardRadius, 0.0]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [cardWidth/2-2*cardRadius, cardHeight/2-cardRadius, 0.0,
                    cardWidth/2, cardHeight/2-cardRadius, 0.0,
                    cardWidth/2, -cardHeight/2+cardRadius, 0.0,
                    cardWidth/2-2*cardRadius, -cardHeight/2+cardRadius, 0.0]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2+cardRadius, -cardHeight/2+2*cardRadius, 0.0,
                    cardWidth/2-cardRadius, -cardHeight/2+2*cardRadius, 0.0,
                    cardWidth/2-cardRadius, -cardHeight/2, 0.0,
                    -cardWidth/2+cardRadius, -cardHeight/2, 0.0]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2, -cardHeight/2+cardRadius, zi,
                    -cardWidth/2, cardHeight/2-cardRadius, zi,
                    -cardWidth/2+2*cardRadius, cardHeight/2-cardRadius, zi,
                    -cardWidth/2+2*cardRadius, -cardHeight/2+cardRadius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2+cardRadius, cardHeight/2-2*cardRadius, zi,
                    -cardWidth/2+cardRadius, cardHeight/2, zi,
                    cardWidth/2-cardRadius, cardHeight/2, zi,
                    cardWidth/2-cardRadius, cardHeight/2-2*cardRadius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [cardWidth/2-2*cardRadius, cardHeight/2-cardRadius, zi,
                    cardWidth/2, cardHeight/2-cardRadius, zi,
                    cardWidth/2, -cardHeight/2+cardRadius, zi,
                    cardWidth/2-2*cardRadius, -cardHeight/2+cardRadius, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2+cardRadius, -cardHeight/2+2*cardRadius, zi,
                    cardWidth/2-cardRadius, -cardHeight/2+2*cardRadius, zi,
                    cardWidth/2-cardRadius, -cardHeight/2, zi,
                    -cardWidth/2+cardRadius, -cardHeight/2, zi]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', front))
            vertex = [-cardWidth/2, -cardHeight/2+cardRadius, 0.0,
                        -cardWidth/2, cardHeight/2-cardRadius, 0.0,
                        -cardWidth/2, cardHeight/2-cardRadius, zi,
                        -cardWidth/2, -cardHeight/2+cardRadius, zi
            ]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', edge))
            vertex = [-cardWidth/2+cardRadius, cardHeight/2, 0.0,
                        cardWidth/2-cardRadius, cardHeight/2, 0.0,
                        cardWidth/2-cardRadius, cardHeight/2, zi,
                        -cardWidth/2+cardRadius, cardHeight/2, zi
            ]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', edge))
            vertex = [cardWidth/2, cardHeight/2-cardRadius, 0.0,
                        cardWidth/2, -cardHeight/2+cardRadius, 0.0,
                        cardWidth/2, -cardHeight/2+cardRadius, zi,
                        cardWidth/2, cardHeight/2-cardRadius, zi
            ]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', edge))
            vertex = [-cardWidth/2+cardRadius, -cardHeight/2, 0.0,
                        cardWidth/2-cardRadius, -cardHeight/2, 0.0,
                        cardWidth/2-cardRadius, -cardHeight/2, zi,
                        -cardWidth/2+cardRadius, -cardHeight/2, zi
            ]
            self.batch.add(4, GL_QUADS, self.edges, ('v3f', vertex), ('c3f', edge))
    def DrawCylinders(self):
        glPushMatrix()
        glTranslatef(-cardWidth/2+cardRadius, -cardHeight/2+cardRadius, 0.0)
        self.cylinder.draw()
        glTranslatef(0.0, cardHeight-2*cardRadius, 0.0)
        self.cylinder.draw()
        glTranslatef(cardWidth-2*cardRadius, 0.0, 0.0)
        self.cylinder.draw()
        glTranslatef(0.0, -cardHeight+2*cardRadius, 0.0)
        self.cylinder.draw()
        glPopMatrix()
    def createField(self, side):
        if(side == 'front'):
            depth = 0.1
            group = self.front_tex
        else:
            depth = self.depth-0.1
            group = self.back_tex
        batch = Batch()
        vertex = [-cardWidth/2+cardRadius, -cardHeight/2+cardRadius, depth,
                -cardWidth/2+cardRadius, cardHeight/2-cardRadius, depth,
                cardWidth/2-cardRadius, cardHeight/2-cardRadius, depth,
                cardWidth/2-cardRadius, -cardHeight/2+cardRadius, depth]
        color = [1.0, 0.0, 0.0] * 4
        tex_coords = [0.0,0.0, 0.0,0.575, 0.8,0.575, 0.8,0.0]
        batch.add(4, GL_QUADS, group, ('v3f', vertex), ('t2f', tex_coords))
        return batch
        #return vertex_list(4, ('v3f', vertex), ('c3f', color), ('t2f', tex_coords))
    def get_tex(self, file):
        tex = image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        return TextureGroup(tex)
    def assign_texture(self):
        if (self.color == None):
            self.color = ''
        self.back_tex = self.get_tex('cardTextures/back.png')
        loc = 'cardTextures/'
        self.front_tex = self.get_tex(loc + self.name + self.color + '.png')
        #if(self.name == 'colorChange'):
        #    self.front_tex = self.get_tex('cardTextures/colorChange.png')
        #elif(self.name == 'stop'):
        #    self.front_tex = self.get_tex(loc + 'stop.png')
        #else:
        #    self.front_tex = self.get_tex(loc + self.name + self.color + '.png')

    def __init__(self, name, color):
        self.batch = Batch()
        self.depth = -2.0
        self.edges = Group()
        self.rotation = 0.0
        self.x = 0
        self.px = 0
        self.y = 0
        self.py = 0
        self.name = name
        self.color = color
        self.moving = False
        self.moving_speed = 5.0
        self.zRot = 0
        self.pzRot = 0

        #declare elements
        self.selected = False
        self.cylinder = Cylinder(cardRadius, self.depth, [1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.CreateEdges([1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.assign_texture()
        self.front = self.createField('front')
        self.back = self.createField('back')
    def setOrder(self, number):
        self.depth += number*0.2
    def move(self):
        #moving X
        if(self.px == self.x):
            self.px = self.x
        elif(abs(self.px - self.x) < self.moving_speed):
            self.px = self.x
        else:
            if(self.px < self.x):
                self.px += self.moving_speed
            else:
                self.px -= self.moving_speed

        #moving Y
        if(self.py == self.y):
            self.py = self.y
        elif(abs(self.py - self.y) < self.moving_speed):
            self.py = self.y
        else:
            if(self.py < self.y):
                self.py += self.moving_speed
            else:
                self.py -= self.moving_speed

        if(self.py == self.y and self.px == self.x):
            self.moving = False
    def draw(self):
        if (self.selected):
            add = 20.0
        else:
            add = 0.0
        glPushMatrix()
        glTranslatef(self.px, self.py, self.depth + add)
        glRotatef(self.rotation, 0, 1, 0)
        glRotatef(self.pzRot, 0, 0, 1)
        if (self.selected):
                glScalef(1.25, 1.25, 1.25)
        self.batch.draw()
        self.DrawCylinders()
        self.front.draw()
        self.back.draw()
        glPopMatrix()
