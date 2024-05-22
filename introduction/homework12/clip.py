from media import Media

class Clip (Media) :
    def __init__(self, type, name, director, duration, url, imbd_score):
        super().__init__(type, name, director, duration, url, imbd_score)