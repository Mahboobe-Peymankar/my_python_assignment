import arcade
import arcade.color

COLUMN_SPACING = 10
ROW_SPACING = 10
LEFT_MARGIN = 150
BOTTOM_MARGIN = 150


# arcade.open_window(400, 400, "Complex Loops - box")

# arcade.set_background_color(arcade.color.WHITE)

# arcade.start_render()


# for row in range (10):
#     for column in range (10):
                
#         x = column * COLUMN_SPACING  + LEFT_MARGIN
#         y = row * ROW_SPACING  + BOTTOM_MARGIN
#         if (row + column) % 2 == 0 :
#             arcade.draw_ellipse_filled(x , y, 8 , 8 , arcade.color.BLUE )
#         else :
#             arcade.draw_ellipse_filled(x , y, 8 , 8 , arcade.color.RED )

# arcade.finish_render()



class Pattern (arcade.Sprite) :
    def __init__(self , n_row , n_col):
        self.n_row = n_row
        self.n_col = n_col

    def generate_pattern (self , row , col) :
           
        x = col * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN
        if (row + col) % 2 == 0 :
            color = arcade.color.BLUE

        else :
            color = arcade.color.RED
        
        return x, y , color





        

class Draw_Board (arcade.Window):

    def __init__ (self):
        super().__init__ (width = 400 , height= 400, title= "Complex Loop -Box")
        arcade.set_background_color (arcade.color.WHITE ) 
        self.pattern = Pattern (10,10)

    def on_draw(self):
        arcade.start_render ()

        for row in range (self.pattern.n_row):
            for column in range (self.pattern.n_col):
                center_x, center_y , color = self.pattern.generate_pattern (row , column)
                arcade.draw_ellipse_filled (center_x , center_y, 8 , 8 , color)

board = Draw_Board ()
arcade.run()



        

