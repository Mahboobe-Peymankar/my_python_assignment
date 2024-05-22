from media import Media 
from actor import Actor

MEDIA = []
ACTORS = []
class app :
    def __init__ (self):
        ...
    
    @staticmethod
    def show_menu ():
        print ("1- Add")
        print ("2- Edit")
        print ("3- Remove")
        print ("4- Search")
        print ("5- Show_list")
        print ("6- add_casts")
        print ("7- download")
        print ("8- Exit")

    @staticmethod
    def read():
        f = open ("database.txt","r")

        for line in f :
            result = line.split (",")
            my_Media = Media (result [0] , result [1] , result [2] , result [3] , result [4] , "score")
            MEDIA.append (my_Media)
        
        # for media in MEDIA :
        #     print (media.show_info())
        
        f.close ()
    @staticmethod
    def read_actor():
        f = open ("actor.txt","r")

        for line in f :
            film = []
            result = line.split (",")
           
            no_film = len (result) - 3
            for i in range (3 , 3 + no_film  ):
                film.append (result [i].replace ("\n",""))
        
            my_actor = Actor (result [0] , result [1] , result [2] )
            my_actor.film = film
            ACTORS.append (my_actor)
        
       
        f.close ()
    @staticmethod
    def write ():
        f = open ("database.txt","w")

        for media in MEDIA :
            line = media.type + "," + media.name + "," + media.director + "," + media.duration + "," + media.imbd_score + "\n"
            print (line)
            f.write (line)

        f.close ()
 


print ("Welcome to my MEDIA app")
print ( "Loading...")
app.read ()
app.read_actor ()

print ("Data loaded")


while True:
    app.show_menu()
    choice = int ( input ("Enter your choice: " ) )
    
    if choice == 1 :
        new_media = Media.add ()
        MEDIA.append (new_media)

    elif choice == 2 :
        name = input ("enter a name of the media: ")
        for media in MEDIA:
            if media.name == name :
                media.edit()
                print ("data has been edited successfully")
                break
        else :
           print ("no media with this name was found")

    elif choice == 3 :
        name = input ("enter a name of the media: ")
        for media in MEDIA:
            if media.name == name :
                media.remove()
                break
        else :
            print ("no media with this name was found")
          
    elif choice == 4 :
        media_name = []
        l = int (input ("enter minimum duration of media..." ))
        u = int (input ("enter maximum duration of media..." ))


        for media in MEDIA :
            # if  l <= int (media.duration) <= u :
            #     media_name.append (media.name)
            
            result = media.search (l,u)
           
            if result != None :
                media_name.append ( result )

        if len (media_name) == 0 :
            print ("no media with this duration limit was found")
        
        else :
            print (media_name)
       

    elif choice == 5 :
        for media in MEDIA :
            media.show_info ()

    elif choice == 6 :
        for media in MEDIA :
            media.add_casts (ACTORS)

    elif choice == 7 :
        name = input ("enter a name of the media: ")
        for media in MEDIA:
            if media.name == name :
                media.download()
                break
        else :
            print ("no media with this name was found")
                
    
    elif choice == 8 :
        app.write ()
        exit (0)
    
    else:
        print ("Invalid input")
