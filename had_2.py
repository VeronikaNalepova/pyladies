import pyglet
from pyglet.window import key
import random
import math

key_press = set()

batch = pyglet.graphics.Batch()
pic_snake = pyglet.image.load('tail-head.png')
ap_food = pyglet.image.load("apple.png")
snake_little = pyglet.image.load("had2.png")
music_game = pyglet.media.load("Snake_game.mp3", streaming=False)
bum_noise = pyglet.media.load("BUM.wav", streaming=False)
dead_song = pyglet.media.load("Dead1.wav", streaming=False)
eat_app = pyglet.media.load("eat_app.wav", streaming=False)
music_game.play()

class State():

    def __init__(self):

        self.snake_position = [(0,0), (0,1), (0,2)]
        self.food_position = []
        self.food_sprite = []
        self.direction = ( 0, 1)
        self.snake_width =20
        self.snake_height = 10
        self.snake_sprites = []
        self.snake_alive = True
        self.press_pause = True
        self.pause_label = True

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
                food_x = random.randint(0, 20)
                food_y = random.randint(0, 10)
                if (food_x, food_y) not in self.snake_position and (food_x, food_y) not in self.food_position:
                    self.food_position.append((food_x, food_y))
                    new_food = pyglet.sprite.Sprite(ap_food, x = food_x*64, y = food_y*64, batch=batch)
                    self.food_sprite.append(new_food)
                return

        return self.food_sprite, self.food_position


    def snake_move(self):
        """Move snake and create new head"""

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
        if self.snake_alive == False and life.num_snake_live > 0:
            bum_noise.play()
            life.num_snake_live -= 1
            self.__init__()
            life.snake_live()
            return

        if self.snake_alive == False and life.num_snake_live == 0:
            pyglet.clock.unschedule(move)
            game_over_lable = pyglet.text.Label(text="GAME OVER", font_name="Terminus", font_size = 36, x=500, y=320, batch = batch)
            dead_song.play()

        """Snake eat a food"""
        if new_head in self.food_position:
            del self.food_sprite[0]
            del self.food_position[0]
            eat_app.play()
            self.food_create()
        else:
            del self.snake_position[0]

        self.snake_position.append(new_head)

        self.snake_draw()



state = State()


class Life():
    def __init__(self):
        self.num_snake_live = 5
        self.snake_lives = []

    def snake_live(self):

        self.snake_lives.clear()
        for i in range(self.num_snake_live):
            live_sprite = pyglet.sprite.Sprite(snake_little, x= 1240-i*25, y= 610, batch = batch)
            live_sprite.scale = 0.2
            self.snake_lives.append(live_sprite)
        return self.snake_lives



life = Life()
life.snake_live()




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

    if symbol == key.SPACE:
        if state.press_pause == True:
            pyglet.clock.unschedule(move)

            #pause_label = pyglet.text.Label(text="PAUSE", font_name="Terminus", font_size = 36, x=180, y=320, batch=batch)
            state.press_pause = False

        elif state.press_pause == False:
            pyglet.clock.schedule_interval(move, 1/6)

            #pause_label = pyglet.text.Label(text="PAUSE", font_name="Terminus", font_size = 36, color = (0,0,0,9000), x=180, y=320, batch=batch)
            state.press_pause = True






def draw():
    window.clear()
    batch.draw()



def move(dt):
    state.snake_move()


pyglet.clock.schedule_interval(move, 1/6)

window = pyglet.window.Window(1280, 640)

window.push_handlers(
    on_draw = draw,
    on_key_press = on_key_press,
)



pyglet.app.run()
