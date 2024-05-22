first_number = int ( input ( "enter the first number ...") )
second_number = int ( input ( "enter the first number ...") )

if first_number < second_number :
    lcm = second_number
else :
    lcm = first_number

while True :
    if lcm % first_number == 0 and lcm % second_number == 0 :
        print ( "lcm = " , lcm )
        break
    else:
        lcm += 1
