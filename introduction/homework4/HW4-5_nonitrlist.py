list = []
while True :
    list.append ( int (input ( "enter a number to add to list..." ) ) )
    print ( list )
    if input( "please enter exit to print an unique list..." ) == "exit" :
        break
print ( "input list :" , list )

unique_list = []
for item in list :
    if item not in unique_list:
        unique_list.append ( item )

print ( "unique list :" , unique_list )