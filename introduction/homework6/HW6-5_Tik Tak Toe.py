import pyfiglet
import random
import time
from colorama import Fore

title = pyfiglet.figlet_format ( "Tic Tac Toe" , font = "slant"  )
print ( title )


def show ():
    for row in game_board :
        for cell in row :
            if cell == "X" :
                print ( Fore.RED , cell , Fore. RESET , end = " ")
            elif cell == "O":
                print ( Fore.BLUE , cell , Fore. RESET , end = " ")
            else :
                print (cell , end = " ")
            
        print ("")



def choose_location ( No_player :int):
    while True:
        if No_player != 3 :
            row = int (input ( "row: ") )
            col = int (input ( "col: ") )
        else :
            row = random.randint (0,2)
            col = random.randint (0,2)

        if 0 <= row <= 2 and 0 <= col <= 2  :
            if game_board [row] [col] == " - ":
                if No_player == 1 :
                    game_board [row] [col] = "X"
                    player_1 [0] [row] += 1
                    player_1 [1] [col] += 1
                    if row == col :
                        player_1 [2][0] += 1
                    
                else :
                    game_board [row] [col] = "O"
                    player_2 [0] [row] += 1
                    player_2 [1] [col] += 1
                    if row == col :
                        player_2 [2][0] += 1
                    
                break
            else :
                print ("jer nazan :/ ")
        else:
            print ("out of range")
            print ("  TRY AGAIN  ")


    
def check_game (No_player :int , End :int) :
    
    if No_player == 1 and any ( 3 in sub for sub in player_1 ):
        print ("You WIN")
        End = 1
        
    elif No_player != 1 and any ( 3 in sub for sub in player_2 ):
        if mode == 1:
            print ("Player 2 wins")
        else:
            print( "computer wins")
        End = 1 
            
   
    if count == 9 and End == 0 :
        print ( "     TIE       \n Both players were equal ")
        End = 1
    
    return End
        


while True:
    mode = int (input ("0: play with computer, 1: play with 2 players ..."))
    if mode == 0 :
        print ("play with computer")
        print("--------------------")
        break
    elif mode == 1 :
        print ("two player game")
        print("--------------------")
        break
    else:
        print ("invalid data. TRY AGAIN")


   
start_time = time.time ()

game_board = [[" - " , " - " , " - "],
              [" - " , " - " , " - "],
              [" - " , " - " , " - "] ]

show ()


player_1 = [[ 0 , 0 , 0 ],
            [ 0 , 0 , 0 ],
            [0]]

player_2 = [[ 0 , 0 , 0 ],
            [ 0 , 0 , 0 ],
            [0]]

count = 0
while True :
    End = 0
    
    no_player = 1
    print ("Turn of Player 1 ")
        
    choose_location ( no_player )
    count += 1
    show ( )
    if check_game ( no_player , End) == 1 :
        break


    print ("-------------------------------")

        
    if mode == 1 : 
        no_player = 2
        print ("Turn of Player 2")
        choose_location ( no_player )
    else :
        no_player = 3
        print ("Turn of computer")
        choose_location ( no_player )
    show ()
    count += 1
    if check_game ( no_player , End) == 1 :
        break
    print ("-------------------------------")

finish_time = time.time ()
print ("Time elapsed (in sec ) =  ", finish_time-start_time)