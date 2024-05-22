first_number = int ( input ( "enter the first number ...") )
second_number = int ( input ( "enter the first number ...") )

if first_number > second_number :
    gcd = second_number
else :
    gcd = first_number

while gcd >= 1 :
    if  first_number % gcd == 0 and second_number % gcd == 0 :
        print ( "gcd = " , gcd )
        break
    else:
        gcd -= 1
