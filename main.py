import pyglet as pg
import entities

distance = 500.0
rotOX = 0.0
rotOY = 0.0
entities.xRadius = 368.0
entities.yRadius = 207.0

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

        #deck
        entities.deck = entities.Deck(-40.0)
        entities.usedDeck = entities.Used()
        #players
        self.player1 = entities.Player(0, True, self)
        self.player2 = entities.Player(1, False, self)
        self.player3 = entities.Player(2, False, self)
        self.player4 = entities.Player(3, False, self)
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
        entities.deck.draw()
        entities.usedDeck.draw()
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
        entities.usedDeck.update(dt)
        print(pg.clock.get_fps())

if __name__ == '__main__':
    config = pg.gl.Config(sample_buffers=1, samples=4)
    window = Window(width=1280, height=720, caption='UNO', config=config, resizable=True)
    pg.gl.glClearColor(0.5, 0.7, 1, 1)
    pg.gl.glEnable(pg.gl.GL_DEPTH_TEST)
    pg.app.run()