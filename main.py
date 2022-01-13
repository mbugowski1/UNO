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
        self.button_pressed = False
        if(position == 0 or position == 2):
            self.maxSize = xRadius - 168.0
        elif(position == 1 or position == 3):
            self.maxSize = yRadius - 107.0
    def update(self, dt, keys):
        if(self.playable):
            self.select(dt, keys)
        for card in self.cards:
            if(card.moving):
                card.move()
    def select(self, dt, keys):
        if(self.button_pressed == False):
            if(keys[pg.window.key.A]):
                if(self.selectedIndex > 0):
                    self.cards[self.selectedIndex].selected = False
                    self.selectedIndex -= 1
                    self.cards[self.selectedIndex].selected = True
                    self.button_pressed = True
            elif(keys[pg.window.key.D]):
                if(self.selectedIndex < len(self.cards) - 1):
                    self.cards[self.selectedIndex].selected = False
                    self.selectedIndex += 1
                    self.cards[self.selectedIndex].selected = True
                    self.button_pressed = True
        else:
            if(keys[pg.window.key.A] == False and keys[pg.window.key.D] == False):
                self.button_pressed = False
    def addCards(self, count):
        self.selectedIndex = 0
        for x in range(count):
            card = Card('stop', None)
            if(self.position == 0):
                card.zRot = 0.0
            elif(self.position == 1):
                card.zRot = 90.0
            elif(self.position == 2):
                card.zRot = 180.0
            elif(self.position == 3):
                card.zRot = 270.0
            if(self.playable):
                card.yRot = 180.0
            self.cards.append(card)
        self.positionCards()
        if(self.playable):
            self.cards[self.selectedIndex].selected = True
    def positionCards(self):
        if (len(self.cards)%2 == 0):
            parzyste = cardWidth/2+5
        else:
            parzyste = 0.0
        if(self.position % 2 == 0):
            horizontal = True
        else:
            horizontal = False
        lewo = 1
        counter = 0
        for card in self.cards:
            if(horizontal):
                card.x = lewo * (parzyste + counter * (cardWidth + 10) )
            else:
                card.y = lewo * (parzyste + counter * (cardWidth + 10) )
            if (lewo == 1 and parzyste == 0.0):
                counter += 1
            elif (lewo != 1 and parzyste != 0.0):
                counter += 1
            lewo *= -1

        def sorting(e):
            if(horizontal):
                return e.x
            else:
                return e.y
        self.cards.sort(key=sorting)
        for x in range(len(self.cards)):
            self.cards[x].setOrder(x)
            if(horizontal):
                if (self.cards[len(self.cards)-1].x > self.maxSize):
                    self.cards[x].x *= self.maxSize/self.cards[len(self.cards)-1].x
            if(self.position == 0):
                self.cards[x].y = -yRadius + cardHeight/2 + 20
            elif(self.position == 2):
                self.cards[x].y = (-yRadius + cardHeight/2 + 20) * -1
            elif(self.position == 1):
                self.cards[x].x = -xRadius + cardHeight/2 + 20
            elif(self.position == 3):
                self.cards[x].x = (-xRadius + cardHeight/2 + 20) * -1
            self.cards[x].moving = True
    def draw(self):
        pg.graphics.glPushMatrix()
        for card in self.cards:
            card.draw()
        pg.graphics.glPopMatrix()
class Window(pg.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300, 200)
        self.keys = pg.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        pg.clock.schedule_interval(self.update, 1/60.0)
        pg.gl.glMatrixMode(pg.gl.GL_PROJECTION)
        pg.gl.glLoadIdentity()
        pg.gl.gluPerspective(45.0, self.width/self.height, 1.0, 1000.0)
        pg.gl.glMatrixMode(pg.gl.GL_MODELVIEW)
        pg.gl.glLoadIdentity()

        self.player1 = Player(0, True, self)
        self.player2 = Player(1, False, self)
        self.player3 = Player(2, False, self)
        self.player4 = Player(3, False, self)
        self.player1.addCards(3)
        self.player2.addCards(5)
        self.player3.addCards(11)
        self.player4.addCards(3)

    def on_resize(self, width, height):
        pg.gl.glViewport(0, 0, width, height)
    def on_draw(self):
        self.clear()
        pg.graphics.glPushMatrix()
        pg.graphics.glTranslatef(0, 0, -distance)
        pg.graphics.glRotatef(rotOX, 1, 0, 0)
        pg.graphics.glRotatef(rotOY, 0, 1, 0)
        #drawing models
        self.player1.draw()
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()
        pg.graphics.glPopMatrix()
    def update(self, dt):
        self.player1.update(dt, self.keys)
        self.player2.update(dt, self.keys)
        self.player3.update(dt, self.keys)
        self.player4.update(dt, self.keys)
        print(pg.clock.get_fps())

if __name__ == '__main__':
    config = pg.gl.Config(sample_buffers=1, samples=4)
    window = Window(width=1280, height=720, caption='UNO', config=config, resizable=True)
    pg.gl.glClearColor(0.5, 0.7, 1, 1)
    pg.gl.glEnable(pg.gl.GL_DEPTH_TEST)
    pg.app.run()