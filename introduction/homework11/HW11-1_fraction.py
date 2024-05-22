class Fraction :
    def __init__ (self , numerator , denominator) :
        self.numerator = numerator
        self.denominator = denominator
        self.show ()
    

    def sum (self , other  ):
        result_n = self.numerator * other.denominator + self.denominator * other.numerator
        result_d = self.denominator * other.denominator
        result = Fraction (result_n , result_d)
        return result
        
    
    def subtract (self , other ):
        result_n = self.numerator * other.denominator - self.denominator * other.numerator
        result_d = self.denominator * other.denominator
        result = Fraction (result_n , result_d)
        return result

    def division (self , other ):
        result_n = self.numerator * other.denominator 
        result_d = self.denominator * other.numerator
        result = Fraction (result_n , result_d)
        return result
    
    def multiply (self , other ):
       result_n = self.numerator * other.numerator 
       result_d = self.denominator * other.denominator
       result = Fraction (result_n , result_d)
       return result

    def frac_to_number (self):
        dec_num = self.numerator / self.denominator
        return dec_num
    
    def simplify (self):
        if self.numerator > self.denominator :
            gcd = self.denominator  
        else :
            gcd = self.numerator

        while gcd >= 1 :
            if  self.numerator % gcd == 0 and self.denominator % gcd == 0 :
                result_n = int (self.numerator / gcd )
                result_d= int (self.denominator / gcd )
                return Fraction (result_n, result_d)
                break
            else:
                gcd -= 1


    def show (self):
        print (self.numerator, "/",self.denominator)

print ("Welcome to my Fraction class" )
while True :
    print ("select a method defined below")
    print ("-----------------------------")
    print ("0 : exit")
    print ("1: sum 2 fractions")
    print ("2: subtract 2 fractions")
    print ("3: multiply 2 fractions")
    print ("4: divide 2 fractions")
    print ("5: convert a fraction to a decimal number")
    print ("6: simplify a fraction")
    print ("7: show a fraction")

    request = int (input ("please select your request from above menu: "))
    if request == 0 :
        break
    elif 1<= request <= 7 :
        num_1 = int(input ("enter your numerator  "))
        denom_1 =int(input ("enter your denominator  "))
        fraction1 = Fraction ( num_1, denom_1 )

        if request <= 4 :
            num_2 = int(input ("enter your numerator  "))
            denom_2 =int(input ("enter your denominator  "))        
            fraction2 = Fraction ( num_2, denom_2)

            if request == 1 :
                s = fraction1.sum (fraction2)
            
            elif request == 2 :
                m = fraction1.subtract (fraction2)

            elif request == 3 :
                p = fraction1.multiply (fraction2)

            elif request == 4 :
                d = fraction1.division (fraction2)

        else :
            if request == 5 :
                n = fraction1.frac_to_number()

            elif request == 6 :
                simple_frac = fraction1.simplify ()
    else:
        print ("please type a correct request")

