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
        self.cards = [Card(0, 0)]

        self.cards[0].back.colors = [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0]
    def draw(self):
        pg.graphics.glPushMatrix()
        print(self.window.height)
        pg.graphics.glTranslatef(0.0, 100.0, 0.0)
        self.cards[0].draw()
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

        self.player = Player(0, False, self)
        self.quad = pg.graphics.vertex_list(4, ('v3f', [368.0, 207.0, 0.0, 368.0, -207.0, 0.0, -100.0, -100.0, 0.0, -100.0, 100.0, 0.0]))

    def on_resize(self, width, height):
        pg.gl.glViewport(0, 0, width, height)
    def on_draw(self):
        self.clear()
        pg.graphics.glPushMatrix()
        pg.graphics.glTranslatef(0, 0, -distance)
        pg.graphics.glRotatef(rotOX, 1, 0, 0)
        pg.graphics.glRotatef(rotOY, 0, 1, 0)
        #drawing models
        #self.player.draw()
        self.quad.draw(pg.graphics.GL_QUADS)
        #self.verticalLine.draw(pg.graphics.GL_TRIANGLES)
        pg.graphics.glPopMatrix()
        

if __name__ == '__main__':
    config = pg.gl.Config(sample_buffers=1, samples=4)
    window = Window(width=1280, height=720, caption='UNO', config=config, resizable=True)
    pg.gl.glClearColor(0.5, 0.7, 1, 1)
    pg.gl.glEnable(pg.gl.GL_DEPTH_TEST)
    pg.app.run()