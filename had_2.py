import pyglet
from pyglet.window import key
import random
import math

key_press = set()

batch = pyglet.graphics.Batch()
pic_snake = pyglet.image.load('green.png')
ap_food = pyglet.image.load("apple.png")

class State():

    def __init__(self):
        self.snake_position = [(0,0), (0,1), (0,2)]
        #self.food_position = []
        self.direction = ( 0, 1)
        self.snake_width = 64
        self.snake_height = 64
        self.snake_sprites = []

    def snake_draw(self):
        self.snake_sprites.clear()
        for x, y in self.snake_position:
            self.snake_sprites.append(pyglet.sprite.Sprite(pic_snake, x=x*64, y=y*64, batch=batch))

        batch.draw()

    def snake_move(self):
        old_x, old_y = self.snake_position[-1]
        dir_x, dir_y = self.direction
        new_x = old_x + dir_x
        new_y = old_y + dir_y
        new_head = new_x, new_y

        if new_x < 0:
            exit("Game over you are dead")
        if new_y < 0:
            exit("Game over you are dead")
        if new_x + self.snake_width > window.width:
            exit("Game over you are dead")
        if new_y + self.snake_height > window.height:
            exit("Game over you are dead")

        self.snake_position.append(new_head)
        del self.snake_position[0]



state = State()


def on_key_press(symbol, modifier):
    """ Move snake"""

    if symbol == key.UP:
        state.direction = (0, 1)
    if symbol == key.DOWN:
        state.direction = (0, -1)
    if symbol == key.RIGHT:
        state.direction = (1, 0)
    if symbol == key.LEFT:
        state.direction = (-1, 0)


def draw():
    window.clear()
    state.snake_draw()



def move(dt):
    state.snake_move()


pyglet.clock.schedule_interval(move, 1/6)

window = pyglet.window.Window(640, 640)

window.push_handlers(
    on_draw = draw,
    on_key_press = on_key_press,
)



pyglet.app.run()
