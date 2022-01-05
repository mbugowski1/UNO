import pyglet as pg
from cards import Card
def x(percentage):
    return percentage * window.width / 100
def y(percentage):
    return percentage * window.height / 100

window = pg.window.Window()
pg.gl.glClearColor(0, 1, 0, 1)
label = pg.text.Label('UNO',
                            font_name = "Times New Roman",
                            font_size = 36,
                            x = window.width//2,
                            y = window.width//2,
                            anchor_x = 'center', anchor_y = 'center')
card1 = Card(300, 300)
@window.event
def on_draw():
    window.clear()
    pg.graphics.draw(4, pg.gl.GL_QUADS,
    ('v3i', card1.get3())
    )
    label.draw()
pg.app.run()