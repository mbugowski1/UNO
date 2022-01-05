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
cardImage = pg.image.load('reverse.png')
card2 = pg.sprite.Sprite(cardImage, 100, 150)
card2.scale = 0.3
card2.rotation = 0
card1 = Card(100, 300)
@window.event
def on_draw():
    window.clear()
    label.draw()
    card2.draw()
pg.app.run()