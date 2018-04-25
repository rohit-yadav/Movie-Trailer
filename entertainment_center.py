import fresh_tomatoes
import media
"""
When the object is created in this case the toy_story, the __init__() is
called and the self = toy_story.
so when we mention toy_story.storyline i.e self.storyline so we get the
answer accordingly
"""

# Create instance toy_story
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

# Create another instance Avatar
avatar = media.Movie("Avatar", "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                                "https://www.youtube.com/watch?v=5afGGGsxvEA")
ratatouille = media.Movie("Ratatouille", "A rat in Paris",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                            "https://www.youtube.com/watch?v=U7FjbBws7v4")
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                            "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time",
                                    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                    "https://www.youtube.com/watch?v=FAfR8omt-CY")

# Starting the server to display the movies.
movies_my = [hunger_games, toy_story, avatar, midnight_in_paris, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies_my)

# Checking the Class variable
#print(media.Movie.VALID_RATINGS)

# Checking the pre existing class variables
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
