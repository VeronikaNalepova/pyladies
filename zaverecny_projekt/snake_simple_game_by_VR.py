import pyglet
from pyglet.window import key
import random
import math

key_press = set()

batch = pyglet.graphics.Batch()
pic_snake = pyglet.image.load('tail-head.png')
ap_food = pyglet.image.load("apple.png")
snake_little = pyglet.image.load("had2.png")
wall_snake = pyglet.image.load("green.png")
itp = pyglet.image.load("instruction.png")
music_game = pyglet.media.load("Snake_game.mp3", streaming=False)
bum_noise = pyglet.media.load("BUM.wav", streaming=False)
dead_song = pyglet.media.load("Dead1.wav", streaming=False)
eat_app = pyglet.media.load("eat_app.wav", streaming=False)
level_up = pyglet.media.load("level_up.wav", streaming=False)
win_song = pyglet.media.load("win.wav", streaming=False)
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
        self.num_wall = 6
        self.wall_sprite = []
        self.wall_position = []

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
                if (food_x, food_y) not in self.snake_position and (food_x, food_y) not in self.food_position and (food_x, food_y) not in self.wall_position:
                    self.food_position.append((food_x, food_y))
                    self.food_sprite.append(pyglet.sprite.Sprite(ap_food, x = food_x*64, y = food_y*64, batch=batch))
                    return

        return self.food_sprite, self.food_position

    def wall_create(self):
        """Level-3 Generate wall in random position and add in wall list"""
        for i in range(self.num_wall):
            wall_x = random.randint(1, 20)
            wall_y = random.randint(1, 10)
            if distance((wall_x, wall_y), self.snake_position[0]) < 100 and (wall_x, wall_y) not in self.food_position and (wall_x, wall_y) not in self.wall_position:
                self.wall_position.append((wall_x, wall_y))
                self.wall_sprite.append(pyglet.sprite.Sprite(wall_snake, x = wall_x * 64, y = wall_y * 64, batch = batch))

        return self.wall_sprite, self.wall_position


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

        """Snake is in yourself or Snake is in the wall"""
        if new_head in self.snake_position or new_head in self.wall_position:
            self.snake_alive = False


        """When snake is dead and have some lifes"""
        if self.snake_alive == False and life.num_snake_live > 0:
            bum_noise.play()
            if life.snake_level == 1 or life.snake_level == 2:
                life.num_snake_live -= 1
                self.__init__()
                life.snake_live()
                return
            if life.snake_level == 3:
                life.num_snake_live -= 1
                self.__init__()
                life.snake_live()
                self.num_wall +=4
                self.wall_create()
                return


        """When snake is dead = Game over"""
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

        """New level and win game"""
        if len(self.snake_sprites) > 5:
            self.__init__()
            level_up.play()
            life.snake_level += 1
            life.level()
            pyglet.clock.unschedule(move)
            move_speed()
            if life.snake_level == 3:
                self.wall_create()
                life.level()
            if life.snake_level == 4:
                win = pyglet.text.Label(text="YOU WIN !!!", font_name="Terminus", font_size = 36, x=500, y=320, batch = batch)
                pyglet.clock.unschedule(move)
                win_song.play()
            return

        self.snake_position.append(new_head)
        self.snake_draw()

state = State()


class Life():
    """Create number life in game in right top window"""

    def __init__(self):
        self.num_snake_live = 5
        self.snake_lives = []
        self.snake_level = 1
        self.level_sprite = []

    def snake_live(self):
        """Create live sprite in top of widow"""

        self.snake_lives.clear()
        for i in range(self.num_snake_live):
            live_sprite = pyglet.sprite.Sprite(snake_little, x= 1240-i*25, y= 610, batch = batch)
            live_sprite.scale = 0.2
            self.snake_lives.append(live_sprite)
            live_lable = pyglet.text.Label(text="LIVES:", font_name="Terminus", font_size = 12, x=1080, y=620, batch = batch)
        return self.snake_lives

    def level(self):

        """Create level sprite in top of window"""
        for i in range(self.snake_level):
            level_sprite = pyglet.sprite.Sprite(ap_food, x = 65+i*35, y = 610, batch=batch)
            level_sprite.scale = 0.5
            self.level_sprite.append(level_sprite)
            level_lable = pyglet.text.Label(text="LEVEL:", font_name="Terminus", font_size = 12, x=0, y=620, batch = batch)
        return self.level_sprite



life = Life()
life.snake_live()
life.level()

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


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
            state.press_pause = False
        elif state.press_pause == False:
            move_speed()
            state.press_pause = True

    if symbol == key.ENTER:
        pyglet.clock.unschedule(move)
        instructions_to_play.delete()
        move_speed()



def draw():
    window.clear()
    batch.draw()

def move(dt):
    state.snake_move()


def move_speed():
    """Speed for each level"""
    if life.snake_level == 1:
        pyglet.clock.schedule_interval(move, 1/3)
    if life.snake_level > 1:
        pyglet.clock.schedule_interval(move, 1/6)


instructions_to_play = pyglet.sprite.Sprite(itp, x = 150, y = 150, batch=batch)


window = pyglet.window.Window(1280, 640)

window.push_handlers(
    on_key_press = on_key_press,
    on_draw = draw,

)


pyglet.app.run()
