list = []
while True :
    list.append ( int (input ( "enter a number to add to list..." ) ))
    print ( list )
    if input( "please enter exit to print a reverse list..." ) == "exit" :
        break
print ( "input list :" , list )
reversed_list = []
len = len ( list )
for i in range ( len ) :
    reversed_list.append ( list [len - i - 1] )
print ( "reversed list: " , reversed_list ) 