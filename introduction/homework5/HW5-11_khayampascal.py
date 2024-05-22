def khayyam_pascal ( n ):
    for row in range ( 1 , n + 1 ):
        c = 1
        for col in range ( 1 , row + 1):
            print ( int ( c ) , end = " ")
            c = c * ( row  - col ) / col
        print ("")

khayyam_pascal ( int  ( input  ( "enter a number ...")))
