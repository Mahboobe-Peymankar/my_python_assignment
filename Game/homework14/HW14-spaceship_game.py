
import arcade
import random
from bullet import Bullet
from enemy import Enemy
from spaceship import Spaceship
from heart import Heart
  
 


class Game (arcade.Window):

    def __init__ (self):
        super().__init__ (width = 400 , height=600, title="Spaceship Game 2024")
        arcade.set_background_color (arcade.color.DARK_BLUE) 
        self.background = arcade.load_texture (":resources:images/backgrounds/stars.png")
        self.time_taken = 0
        self.me = Spaceship(self.width) 
        #self.enemy = Enemy (self.width , self.height)
        self.enemy_list = []
       
        self.heart_list = []
             
        while (len (self.heart_list) < 3) :

            new_heart = Heart ()
            new_heart.location_x (len (self.heart_list))
            
            self.heart_list.append (new_heart)
        
        self.score = 0
        self.elapsed_time =0
        self.increasing_speed = 0
        self.game_over = False
        self.laser_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        self.explosion_sound = arcade.load_sound(":resources:sounds/hit3.wav")
        self.laser_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover4.wav")
        self.collision_sound = arcade.load_sound(":resources:sounds/hurt4.wav")
        self.crossover_sound = arcade.load_sound(":resources:sounds/hurt1.wav")

    def on_draw(self):
        arcade.start_render ()
        
        if  self.game_over == False :
            arcade.draw_lrwh_rectangle_textured(0, 0,self.width, self.height,self.background)
            self.me.draw()
            for enemy in self.enemy_list :
                enemy.draw ()

            for bullet in self.me.bullet_list :
                bullet.draw()
            
            for heart in self.heart_list:
                heart.draw ()
        else :
            arcade.set_background_color (arcade.color.BLACK) 
                    
            arcade.draw_text("Game Over", 120, 300, arcade.color.WHITE, font_size= 20)
            arcade.draw_text(f"Score = {self.score} , time = {int (self.time_taken)}", 120, 250, arcade.color.WHITE, font_size= 10)


        
        arcade.draw_text (f"Score = {self.score}" , 300 , 10 , color = arcade.color.GRAY , font_size= 10 )

        arcade.finish_render()
       


    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.me.change_x = -1

        elif symbol == arcade.key.RIGHT or symbol==arcade.key.D:
            self.me.change_x = 1

        elif symbol == arcade.key.DOWN :
            self.me.change_x = 0
        
        elif symbol == arcade.key.SPACE :
            self.me.fire ()
            arcade.play_sound(self.laser_sound)



    def on_key_release(self , symbol: int, modifiers: int):
        self.me.change_x = 0

   
    def on_update (self , delta_time :float):
        
        if self.game_over == False :
            self.time_taken += delta_time
            self.elapsed_time += delta_time
           
            for enemy in self.enemy_list :
                if arcade.check_for_collision (self.me , enemy):
                    print (len(self.heart_list))
                    self.enemy_list.remove(enemy)
                    arcade.play_sound (self.collision_sound)
                    if len(self.heart_list) > 0 :
                        
                        self.heart_list.remove (self.heart_list[len(self.heart_list)-1])
 
                    else:
                        self.clear ()
                        self.game_over = True
                        print ("GAME OVER")

            self.me.move()

            for bullet in self.me.bullet_list:
                bullet.move ()
                if bullet.center_y > self.height :
                    self.me.bullet_list.remove (bullet)

            for enemy in self.enemy_list :    
                enemy.move (self.increasing_speed)
                
            if self.elapsed_time >= 3  :

                self.new_enemy =  Enemy (self.width , self.height)
                self.enemy_list.append (self.new_enemy)
                self.elapsed_time = 0
                self.increasing_speed += 0.05

            for enemy in self.enemy_list :
                for bullet in self.me.bullet_list :
                    if arcade.check_for_collision (enemy , bullet):
                        self.score += 1
                        arcade.play_sound(self.explosion_sound)
                        self.enemy_list.remove(enemy)
                        self.me.bullet_list.remove(bullet)

            
            for enemy in self.enemy_list :
                if enemy.center_y < 0 :
                    self.score -=  1
                    arcade.play_sound (self.crossover_sound)
                    self.enemy_list.remove(enemy)





window = Game ()


arcade.run ()
        