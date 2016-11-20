import webbrowser

class Movie():
    """ Create a doc for Movie Class"""
    
    # Create an instance variable to share
    VALID_RATING = ["G", "PG", "PG-13", "R"]
    
    # Create init instance when it is created
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
    # Create instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)