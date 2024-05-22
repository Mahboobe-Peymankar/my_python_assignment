number = int ( input ( "enter your desired number ..." ) )

fact_check_number = 1
factorial_number = 1


while factorial_number < number :
    fact_check_number += 1
    factorial_number *= fact_check_number
   

if factorial_number == number :
    print ( number , " is a factorial number" )
else :
    print ( number , " is  not a factorial number" )