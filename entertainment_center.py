# Import required modules
import fresh_tomatoes  # Provided script for generating the web page
import media  # My Movies class

# Defining my movie objects
# Defining a base URL to reduce the poster URL to meet PEP8 requirments
wiki_base_url = "https://upload.wikimedia.org/wikipedia/en"  # noqa

# Movie 1
wonder_woman = media.Movie(
            "Wonder Woman",
            wiki_base_url + "/e/ed/Wonder_Woman_%282017_film%29.jpg",
            "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

# Movie 2
the_matrix = media.Movie(
            "The Matrix",
            wiki_base_url + "/c/c1/The_Matrix_Poster.jpg",
            "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Movie 3
sholay = media.Movie(
            "Sholay",
            wiki_base_url + "/5/52/Sholay-poster.jpg",
            "https://www.youtube.com/watch?v=EwT6RdS-Nac")

# Creating the list of movies
movies = [wonder_woman, the_matrix, sholay]

# Generating the movie trailers web page
fresh_tomatoes.open_movies_page(movies)
