import pyglet
from pyglet.window import key
import random
import math

key_press = set()


class State():

    def __init__(self):
        self.snake_position = [(0,0), (0,1), (0,2)]
        #self.food_position = []
        self.direction = ( 0, 1)
        self.snake_width = 64
        self.snake_height = 64

    

    def snake_move(self):
        old_x, old_y = self.snake_position[-1]
        dir_x, dir_y = self.direction
        new_x = old_x + dir_x
        new_y = old_y + dir_y
        new_head = new_x, new_y

        if new_x < 0:
            exit("Game over")
        if new_y < 0:
            exit("Game over")
        if new_x + self.snake_width > window.width:
            exit("Game over")
        if new_y + self.snake_height > window.height:
            exit("Game over")

        self.snake_position.append(new_head)
        del self.snake_position[0]


state = State()

pic_snake = pyglet.image.load('green.png')

ap_food = pyglet.image.load("apple.png")


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

    for x, y in state.snake_position:
        snake = pyglet.sprite.Sprite(pic_snake, x, y)
    snake.draw()


def move(dt):
    state.snake_move()




pyglet.clock.schedule_interval(move, 1/60)


window = pyglet.window.Window(640, 640)

window.push_handlers(
    on_draw = draw,
    on_key_press = on_key_press,

)



pyglet.app.run()
