import pytube
from actor import Actor
class Media (Actor):
    def __init__(self , type , name , director , duration , url , imbd_score ) :
        self.type = type
        self.name = name
        self.director = director
        self.duration = duration
        self.url = url
        self.imbd_score = imbd_score
        self.casts = []

    
    def show_info (self) :
        print ("Name: " , self.name)
        print ("Director: " , self.director)
        print ("IMBD Score:" , self.imbd_score)
        print ("URL: " , self.url)
        print ("Duration: " , self.duration)
        print ("Casts :", self.casts)

    def download (self):
        link = self.url
        first_stream = pytube.YouTube (link) .streams.first ()
        first_stream.download(output_path = "./" , filename= self.name+".mp4" )

    @staticmethod
    def add () :
        type = input ("Enter type:  ")
        name = input ("Enter name:  ")
        director = input ("Enter director:  ")
        duration = input ("Enter duration:  ")
        url = input ("Enter url:  ")
        imbd_score =input ("Enter imbd_score:  ")

        new_media = Media (type , name , director , duration , url , imbd_score)
        return new_media

    def edit (self ):
        print ("1: edit type")
        print ("2: edit name")
        print ("3: edit director")
        print ("4: edit duration")
        print ("5: edit url")
        print ("6: edit imbbd_score")
        choice = int (input ( "type your choice : " ) )
        if choice == 1 :
            self.type = input ("type new type...")
                
        elif choice == 2 :
            self.name = input ("type new name...")

        elif choice == 3 :
            self.director = input ("type new director...")
       
        elif choice == 4 :
            self.duration = input ("type new duration...")

        elif choice == 5 :
            self.url = input ("type new url...")
        
        elif choice == 6 :
            self.imbd_score = input ("type new imbd score...")

        else :
            print ("Invalid choice")

    
    def search ( self , a :int , b :int ) :
        
        if int ( a ) <= int (self.duration ) <= int ( b ) :
            result = self.name
            return result
        
    def add_casts (self,ACTORS):
        for actor in ACTORS :
            if self.name in actor.film :
                self.casts.append (actor.name + " "  +actor.lastname)

        print (self.name,self.casts)






