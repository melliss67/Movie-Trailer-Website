import webbrowser

class Movie():
    """Provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_storyline, poster_url, trailer_url, movie_year, movie_length):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.year = movie_year
        self.length = movie_length

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)
    
