class time :
    def __init__ (self , day , hour , min , sec) :
        self.day = day
        self.hour = hour
        self.min = min
        self.sec =sec    

    def sum (self , time1 , time2 ):
        #sum 2 time
      
        ...
    
    def minus (self , time1 , time2 ):
        #subtract 2 time
        ...

    def to_sec (self ,time1):
        #convert time to second
        ...
    
    def sec_to_time (self , time_in_second ):
        #convert second to day, hour, min and sec
        ...

    def format_24hr (self , time1 ):
        #convert a time to 24hr format
        ...
    
    def format_12hr (self , fraction1 ):
        #convert a time to 12hr format
        ...

time1 = time (int(input ("enter your day  ")) , int(input ("enter your hour")) , int(input ("enter your min")) , int(input ("enter your sec")) )
time2 = time (int(input ("enter your day  ")) , int(input ("enter your hour")) , int(input ("enter your min")) , int(input ("enter your sec")) )
