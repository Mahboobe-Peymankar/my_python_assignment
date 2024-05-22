from media import Media
class Documentary (Media) :
    def __init__(self, type, name, director, duration, url, imbd_score , category):
        super().__init__(type, name, director, duration, url, imbd_score) 
        self.category = category