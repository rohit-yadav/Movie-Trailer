"""
1. class
2. instance
3. constructs
4. self
5. instance variables
6. instance method
"""

import webbrowser
# Class definition
class Movie():
    """
    This class is used to get movies website
    """
    # Class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # function __init__ is called as constructor
    # It constructs space for an instance
    """
    the __init__ is a keyword in python.
    self is not a keyword, self points to the object when object is created.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_yoututbe):
        # Initiatize the variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_yoututbe

# A function defined in a class and is associated with a instance
# is  called instance method

    # Define show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
