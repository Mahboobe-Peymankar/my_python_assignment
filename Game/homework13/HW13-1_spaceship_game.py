import arcade
import random



class Spaceship (arcade.Sprite):
    def __init__ (self,w :float):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w //2
        self.center_y = 80
        self.width = 48
        self.height = 48
        self.speed = 8

class Enemy (arcade.Sprite) :
    def __init__(self,w,h) :
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.width = 48
        self.height = 48
        self.angle = 180

class Game (arcade.Window):

    def __init__ (self):
        super().__init__ (width = 1280 , height=960, title="Spaceship Game 2024")
        arcade.set_background_color (arcade.color.DARK_BLUE_GRAY) 
        self.background = arcade.load_texture (":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width) 
        self.doshman = Enemy (self.width , self.height)

    def on_draw(self):
        arcade.start_render ()
        arcade.draw_lrwh_rectangle_textured(0, 0,self.width, self.height,self.background)
        self.me.draw()
        self.doshman.draw ()

    def on_key_press(self, symbol: int, modifiers: int):
        print ("press one key")
        if symbol == 97:
            self.me.center_x -= 1 * self.me.speed

        elif symbol == 100:
            self.me.center_x += 1 * self.me.speed


window = Game ()


arcade.run ()
        