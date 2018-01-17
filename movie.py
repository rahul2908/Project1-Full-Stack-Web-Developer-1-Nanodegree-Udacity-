import webbrowser

class Films():

    """ This class is build for showing movie trailers. """

    def __init__(self, title, poster_image_url, trailer_youtube_url, duration):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration = duration

    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)

        
