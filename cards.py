from pyglet.graphics import *
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
    def createField(self, depth):
        vertex = [-cardWidth/2+cardRadius, -cardHeight/2+cardRadius, depth,
                -cardWidth/2+cardRadius, cardHeight/2-cardRadius, depth,
                cardWidth/2-cardRadius, cardHeight/2-cardRadius, depth,
                cardWidth/2-cardRadius, -cardHeight/2+cardRadius, depth]
        color = [1.0, 0.0, 0.0] * 4
        return vertex_list(4, ('v3f', vertex), ('c3f', color))
    def __init__(self):
        self.batch = Batch()
        self.depth = -2.0
        self.edges = Group()
        self.rotation = 0.0
        self.x = 0

        #declare elements
        self.selected = False
        self.cylinder = Cylinder(cardRadius, self.depth, [1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.CreateEdges([1.0, 1.0, 1.0], [0.0, 0.0, 0.0])
        self.front = self.createField(0.1)
        self.back = self.createField(self.depth-0.1)
    def setOrder(self, number):
        self.depth += number*0.2
    def draw(self):
        if (self.selected):
            add = 20.0
        else:
            add = 0.0
        glPushMatrix()
        glTranslatef(self.x,0.0, self.depth + add)
        glRotatef(self.rotation, 0, 1, 0)
        if (self.selected):
                glScalef(1.25, 1.25, 1.25)
        self.batch.draw()
        self.DrawCylinders()
        self.front.draw(GL_QUADS)
        self.back.draw(GL_QUADS)
        glPopMatrix()
