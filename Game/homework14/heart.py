import arcade

class Heart (arcade.Sprite):
    def __init__ (self ) :
       
       super().__init__ (":resources:images/items/star.png")
       self.center_x = 10
       self.center_y = 10
       self.width = 30
       self.height = 30
       

    def location_x (self , x):
        self.center_x += x * 30

    