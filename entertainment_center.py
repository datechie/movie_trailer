# Import required modules
import fresh_tomatoes # Provided script for generating the web page
import media # My Movies class

# Defining my movie objects
wonder_woman = media.Movie(
					"Wonder Woman", 
					"https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
					"https://www.youtube.com/watch?v=1Q8fG0TtVAY")

the_matrix = media.Movie(
					"The Matrix", 
					"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					"https://www.youtube.com/watch?v=m8e-FF8MsqU")

sholay = media.Movie(
				"Sholay",
				"https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
				"https://www.youtube.com/watch?v=EwT6RdS-Nac")

# Creating the list of movies
movies = [wonder_woman, the_matrix, sholay]

# Generating the movie trailers web page
fresh_tomatoes.open_movies_page(movies)