import random

computer_number = random.randint ( 10 , 99 )
i = 0
while True :
    user_number = int ( input ( "Enter your guess number..." ) )

    if computer_number == user_number :
        print ( "🌹🌹Congratulation🌹🌹 " )
        print ( "------You Win---------")
        print ( "Number of unsuccessful attempts :", i )
        print ( "Number of attempts :", i+1 )
        break
    
    elif computer_number > user_number :
        print ( "Go UP ⏫⏫" )
    
    else :
        print ( "Go Down ⏬⏬" )