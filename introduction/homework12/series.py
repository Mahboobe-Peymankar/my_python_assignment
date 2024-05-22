from media import Media

class Series (Media):
    def __init__(self, type, name, director, duration, url, imbd_score , session):
        super().__init__(type, name, director, duration, url, imbd_score)
        self. session = session
   