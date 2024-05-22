import random

words_bank = [ "tree" , "book" , "blue" , "sky" , "fish" , "woman" , "life"  , "freedom" , "iran" ]
x = random.randint ( 0 , len ( words_bank ) - 1)
word = words_bank [ x ]

good_chars = []
bad_chars = []

user_mistakes = 0

while ( user_mistakes < 6 ) :
    user_correct_guess = 0
    for i in range ( len ( word ) ) :
        if  word [i] in good_chars:
            print ( word [i]  , end = " " )
            user_correct_guess += 1

        else :
            print ( "_ "  , end = " ")
    
    if user_correct_guess == len ( word ) :
        print ( "" )
        print ( "Congratulation" )
        print ( "🌹YOU WIN🌹" )
        break


    user_char = input ( "Please write your guess ..." )
    user_char = user_char.lower ()
    if len (user_char) == 1 :
        if user_char in word :
            good_chars.append ( user_char )
            print ( "✅" )
        else :
            bad_chars.append ( user_char )
            print ( "❌" )
            user_mistakes += 1
    else :
        print ( "please enter just one char..." )
    
    if user_mistakes == 6 :
        print ( "GAME OVER" )
        print ( "  💀💀  " )

