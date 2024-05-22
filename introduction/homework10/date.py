class date :
    def __init__ (self , year , month , day) :
        self.year = year
        self.month = month
        self.day = day
          

    def sum (self , date1 , date2 ):
        #sum 2 date
      
        ...
    
    def minus (self , date1 , date2 ):
        #subtract 2 date
        ...

    def date_to_hejri_shamsi (self ,date1):
        #convert AD date to hejrishamsi
        ...
    
    def date_to_AD(self , time_in_second ):
        #convert a shamsi date to miladi
        ...

    def compare (self , date1 , date2 ):
        #compare 2 date 
        ...
    
    def format_12hr (self , fraction1 ):
        #convert a time to 12hr format
        ...

time1 = date (int(input ("enter your year  ")) , int(input ("enter your month")) , int(input ("enter your day")) )
time2 = date (int(input ("enter your year  ")) , int(input ("enter your month")) , int(input ("enter your day")) )