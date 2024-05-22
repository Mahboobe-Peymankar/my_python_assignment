class Time :
    def __init__ (self, h , m , s ) :
        self.hr = h
        self.min = m
        self.sec = s
        self.modify ()

    
    def sum (self, other) :
        result_h = self.hr + other.hr
        result_m = self.min + other.min
        result_s = self.sec + other.sec

        result = Time (result_h, result_m , result_s)
        return result

    def subtract (self, other) :
        result_h = self.hr - other.hr
        result_m = self.min - other.min
        result_s = self.sec - other.sec

        result = Time (result_h, result_m , result_s)
        return result
    
    def sec_to_time (self) :
        result_s = self.sec
        result_m = self.min
        result_h =self.hr
        if result_s >= 60 :
            result_m += (result_s // 60)
            result_s -= (60 * result_s// 60)
            

        if result_m>= 60 :
            result_h += (result_m// 60)
            result_m -= (60 * (result_m// 60 ))
            

        result = Time (result_h , result_m , result_s)
        return result
    
    def time_to_second (self) :
        sec = self.sec + 60 * self.min + 3600 * self.hr
        return sec
    
    def to_tehran_time (self) :
        result_m = 30 + self.min
        result_h = 3 + self.hr
        result = Time (result_h , result_m , self.sec)
        return result

    def modify (self):
        
        if self.sec >= 60:
            self.min += (self.sec // 60)
            self.sec -= (60 * (self.sec // 60))
            
        
        if self.min >= 60 :
            self.hr += (self.min // 60)
            self.min -= (60 * (self.min // 60 ))
            
        
        if self.sec < 0 :
            self.min -= (-self.sec // 60 +1)
            self.sec += (60 * (-self.sec // 60 +1))
            
        
        if self.min < 0 :
            self.hr -= (-self.min // 60 + 1)
            self.min += (60 * (-self.min // 60 + 1))
            


    def show (self) :
        print (self.hr ,":" , self.min , ":" , self.sec)


s1 = 120
m1 = 56
h1 = 2

time_1 = Time (h1 , m1 , s1)
time_1.show()

s2 = 20
m2 = 5
h2 = 22

time_2 = Time (h2 , m2 , s2)
time_2.show()

sum = time_1.sum (time_2)
sum.show ()

sub = time_2.subtract (time_1)
sub.show ()

to_sec = time_2.time_to_second ()
print ("time_2 is " , to_sec , "sec")


sec_to_time = Time (0 , 2 , 3400 ).sec_to_time ()
sec_to_time.show ()

tehran_time = Time (6 , 50 ,25).to_tehran_time ()
tehran_time.show ()