def solve_equation3 ( a , b , c , d ) :
    delta =  18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2
    
    delta_0 = b ** 2 - 3 * a * c
    delta_1 = 2*b ** 3 - 9 * a * b * c + 27 * a ** 2 * d    
    delta_2 = -27 * a ** 2 * delta

    C = ( (delta_1 + delta_2 ** 0.5 ) / 2) ** (1/3)

    z = complex ( -1 ,  3 ** 0.5)
    u1 = 1
    u2 = complex ( -1 ,  3 ** 0.5) / 2 
    u3 = complex ( -1 ,  -(3 ** 0.5)) /2

    if delta == 0 :
        x_1 = - ( b ) / ( 3 * a )
        print ("X_1 =" , x_1)

    else :


        x_1 =  - ( b + C * u1  + delta_0 / (C * u1) ) / ( 3 * a )
        x_2 =  - ( b + C * u2  + delta_0 / (C * u2) ) / ( 3 * a )
        x_3 =  - ( b + C * u3  + delta_0 / (C * u3) ) / ( 3 * a )

        print ("X_1 =" , x_1)
        print ("X_2 =" , x_2)
        print ("X_3 =" , x_3)

a = int (input ("enter a  number as coefficient of x^3   "))
b = int (input ("enter a  number as coefficient of x^2   "))
c = int (input ("enter a  number as coefficient of x   "))
d = int (input ("enter a  number as fixed coefficient   "))
solve_equation3 ( a , b , c , d)