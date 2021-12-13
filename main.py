import pyglet as pg


window = pg.window.Window()
label = pg.text.Label('UNO',
                            font_name = "Times New Roman",
                            font_size = 36,
                            x = window.width//2,
                            y = window.width//2,
                            anchor_x = 'center', anchor_y = 'center')
image = pg.resource.image('logo.png')

@window.event
def on_draw():
    window.clear()
    image.blit(0,window.height - image.height - 5)
    label.draw()
pg.app.run()