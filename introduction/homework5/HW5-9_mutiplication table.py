
def mutiplication_table ( n : int , m : int):
    print ( "x" , "     " , end = "")
    for col in range ( 1 , m +1 ) :
        print ( col , "     " , end = "" )
    print ("")    

    for row in range ( 1 , n + 1) :
        for col in range ( m + 1 ):
            if col == 0 :
                print ( row , "     " , end = "")
            else :
                print ( row * col  , "     " , end ="")
        print ("")

mutiplication_table (n = int (input ( "Enter a number of rows ..." ) ),m = int (input ( "Enter a number of columns ..." ) ))
   
