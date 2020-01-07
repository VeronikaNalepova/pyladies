import pyglet
from pyglet.window import key
import random
import math

key_press = set()

pic_snake = pyglet.image.load('green.png')
snake = pyglet.sprite.Sprite(pic_snake)
live_label = pyglet.text.Label(text="Live: 5", x=10, y=600)
ap_food = pyglet.image.load("apple.png")


class State():

    def __init__(self):
        self.snake_position = [0,0]
        #self.direction = "right"
        self.num_food = 20

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def food(num_food, snake_position):
    food =[]
    for i in range(num_food):
        food_x, food_y = snake_position
        while distance((food_x, food_y), snake_position) < 80:
            food_x = random.randint(0,640)
            food_y = random. randint(0,640)
        new_food = pyglet.sprite.Sprite(ap_food, x = food_x, y = food_y)
        food.append(new_food)
    return food




def on_key_press(symbol, modifiers):
    """ Move snake"""
    if symbol == key.UP:
        key_press.add(("up", 0))
    if symbol == key.DOWN:
        key_press.add(("down", 0))
    if symbol == key.RIGHT:
        key_press.add(("right", 0))
    if symbol == key.LEFT:
        key_press.add(("left", 0))

def draw():
    window.clear()
    snake.draw()
    live_label.draw()
    for foods in food:
        food.draw()

def move_snake(t):
    snake.x = snake.x + t * 50

    if snake.x < 0:
        snake.x = 0
    if snake.y < 0:
        snake.y = 0
    if snake.x + snake.width > window.width:
        snake.x = window.width - snake.width
    if snake.y + snake.height > window.height:
        snake.y = window.height - snake.height

pyglet.clock.schedule_interval(move_snake, 1/60)


window = pyglet.window.Window(640, 640)

window.push_handlers(
    on_draw = draw,
    on_key_press = on_key_press,

)



pyglet.app.run()
