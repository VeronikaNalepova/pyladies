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
        self.food_position = []
        self.food_sprite = []
        self.direction = ( 0, 1)
        self.snake_width = 10
        self.snake_height = 10
        self.snake_sprites = []
        self.life = 5
        self.snake_alive = True

        self.food_create()
        self.food_create()

    def snake_draw(self):
        """Create simple snake"""

        self.snake_sprites.clear()
        for x, y in self.snake_position:
            self.snake_sprites.append(pyglet.sprite.Sprite(pic_snake, x=x*64, y=y*64, batch=batch))

    def food_create(self):

        """Generate new food in random position and add in food list"""
        if self.snake_alive == True:
            while True:
                food_x = random.randint(0, 10)
                food_y = random.randint(0, 10)
                if (food_x, food_y) not in self.snake_position and (food_x, food_y) not in self.food_position:
                    self.food_position.append((food_x, food_y))
                    new_food = pyglet.sprite.Sprite(ap_food, x = food_x*64, y = food_y*64, batch=batch)
                    self.food_sprite.append(new_food)
                return

        return self.food_sprite, self.food_position


    def snake_move(self):
        old_x, old_y = self.snake_position[-1]
        dir_x, dir_y = self.direction
        new_x = old_x + dir_x
        new_y = old_y + dir_y

        new_head = new_x, new_y

        """Snake dont move out of Window"""

        if new_x < 0:
            self.snake_alive = False
        if new_y < 0:
            self.snake_alive = False
        if new_x >= self.snake_width:
            self.snake_alive = False
        if new_y >= self.snake_height:
            self.snake_alive = False

        """Snake is in yourself"""
        if new_head in self.snake_position:
            self.snake_alive = False

        """When snake is dead and have some lifes"""
        if self.snake_alive == False and self.life > 0:
            #update()
            self.life -= 1
        else:
            print("Game over")



        """Snake eat a food"""
        if new_head in self.food_position:
            del self.food_sprite[0]
            del self.food_position[0]
            #self.food_sprite.remove(new_head)
            self.food_create()
        else:
            del self.snake_position[0]

        self.snake_position.append(new_head)
        self.snake_draw()



state = State()

def update():
    state = State()
    return state

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
    batch.draw()



def move(dt):
    state.snake_move()


pyglet.clock.schedule_interval(move, 1/6)

window = pyglet.window.Window(640, 640)

window.push_handlers(
    on_draw = draw,
    on_key_press = on_key_press,
)



pyglet.app.run()
