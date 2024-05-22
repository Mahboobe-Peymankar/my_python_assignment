n = int (input ( "please enter a size of aaray ..." ))
array = []
for i in range ( n ) :
    array.append (int (input( "enter a number to add to list ...")))
print (array)
error = 0
for i in range ( n ) :
    for j in range ( i + 1 , n) :
        if array [i] > array [j] :
            print (" not sorted ")
            error = 1
        if (error == 1) :
            break 
    if (error == 1) :
            break        
            
if error == 0 :
    print ("sorted ascending")