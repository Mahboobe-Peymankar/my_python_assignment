
def chess_board (n , m) :
    for row in range ( n ) :
        for col in range ( m ) :
            if ( row + col ) % 2 == 0 :
                print ("#" , end = "")
            else :
                print ("*" , end = "")
        print ("")

chess_board ( n = int (input ( "Enter a number of rows ..." ) ) , m = int (input ( "Enter a number of columns ..." ) ))