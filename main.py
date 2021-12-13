import pyglet as pg


window = pg.window.Window()
label = pg.text.Label('UNO',
                            font_name = "Times New Roman",
                            font_size = 36,
                            x = window.width//2,
                            y = window.width//2,
                            anchor_x = 'center', anchor_y = 'center')
image = pg.resource.image('logo.png')
#image.scale = (min(image.height, window.height)/max(image.height, window.height), max(min(window.width, image.width)/max(window.width, image.width)))

#image.width = window.width
#image.height = window.height
#image.texture.width = window.width
#image.texture.height = window.height

@window.event
def on_draw():
    window.clear()
    pg.graphics.draw_indexed(4, pg.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (0, 0,
                 0, window.height,
                 window.width, window.height,
                 window.width, 0))
    )
    image.blit(0,window.height - image.height - 5)
    label.draw()
pg.app.run()