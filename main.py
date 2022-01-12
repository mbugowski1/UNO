import pyglet as pg
from cards import Card, cardRadius, cardHeight, cardWidth

distance = 500.0
rotOX = 0.0
rotOY = 0.0

xRadius = 368.0
yRadius = 207.0

class Player:
    def __init__(self, position, playable, window):
        self.position = position
        self.playable = playable
        self.window = window
        self.cards = []
        if(position % 2 == 0):
            self.maxSize = window.width - 20.0
        else:
            self.maxSize = window.height - 20.0
    def addCards(self, count):
        for x in range(count):
            self.cards.append(Card())
    def positionCards(self):
        if (len(self.cards)%2 == 0):
            parzyste = cardWidth/2+5
        else:
            parzyste = 0.0
        lewo = 1
        counter = 0
        for card in self.cards:
                    card.x = lewo * (parzyste + counter * (cardWidth + 10) )
                    if (lewo == 1 and parzyste == 0.0):
                        counter += 1
                    elif (lewo != 1 and parzyste != 0.0):
                        counter += 1
                    lewo *= -1
        def sorting(e):
            return e.x
        self.cards.sort(key=sorting)
        for x in range(len(self.cards)):
            self.cards[x].setOrder(x)
            #self.cards[x].x *= 0.5
    def draw(self):
        self.positionCards()
        pg.graphics.glPushMatrix()
        if(self.position == 0 or self.position == 2):
            if (self.position == 2):
                pg.graphics.glRotatef(180, 0, 0, 1)
            pg.graphics.glTranslatef(0.0, -yRadius + cardHeight/2 + 20, 0.0)
        for card in self.cards:
            card.draw()
        pg.graphics.glPopMatrix()
class Window(pg.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300, 200)
        pg.gl.glMatrixMode(pg.gl.GL_PROJECTION)
        pg.gl.glLoadIdentity()
        pg.gl.gluPerspective(45.0, self.width/self.height, 1.0, 1000.0)
        pg.gl.glMatrixMode(pg.gl.GL_MODELVIEW)
        pg.gl.glLoadIdentity()

        self.player = Player(0, True, self)
        self.player3 = Player(2, False, self)
        self.player.addCards(7)
        self.player3.addCards(5)

    def on_resize(self, width, height):
        pg.gl.glViewport(0, 0, width, height)
    def on_draw(self):
        self.clear()
        pg.graphics.glPushMatrix()
        pg.graphics.glTranslatef(0, 0, -distance)
        pg.graphics.glRotatef(rotOX, 1, 0, 0)
        pg.graphics.glRotatef(rotOY, 0, 1, 0)
        #drawing models
        self.player.draw()
        self.player3.draw()
        #self.quad.draw(pg.graphics.GL_QUADS)
        pg.graphics.glPopMatrix()
        

if __name__ == '__main__':
    config = pg.gl.Config(sample_buffers=1, samples=4)
    window = Window(width=1280, height=720, caption='UNO', config=config, resizable=True)
    pg.gl.glClearColor(0.5, 0.7, 1, 1)
    pg.gl.glEnable(pg.gl.GL_DEPTH_TEST)
    pg.app.run()