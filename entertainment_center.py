import fresh_tomatoes # Provided script for generating the web page
import media # My Movies class

#toy_story = media.Movie("Toy Story",
						#"A story of a boy and his toys that come to life",
#						"http://upload.wikimedia.org/wikipedia/en/1/13/Toys_Story.jpg",
#						"https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

#avatar = media.Movie("Avatar", 
					#"A marine on an alien planet",
#					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
#					"http://www.youtube.com/watch?v=-9ceBgWV8io")



# Defining my movie objects
wonder_woman = media.Movie("Wonder Woman", 
					#"A woman Super Hero",
					" https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
					"https://www.youtube.com/watch?v=1Q8fG0TtVAY")

the_matrix = media.Movie(
							"The Matrix", 
							#"A computer hacker learns from mysterious rebels about the true nature of his " + 
							#" reality and his role in the war against its controllers.",
							"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
							"https://www.youtube.com/watch?v=m8e-FF8MsqU"
						)

sholay = media.Movie(
						"Sholay",
						#"After his family is murdered by a notorious and ruthless bandit, a former police officer enlists the services of two outlaws to capture the bandit.",
						"https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
						"https://www.youtube.com/watch?v=EwT6RdS-Nac"

	)
#print(wonder_woman.storyline)
#wonder_woman.show_trailer()

# Creating the list of movies
movies = [wonder_woman, the_matrix, sholay]
#print media.Movie.__name__
#print media.Movie.__module__

# Generating the movie trailers web page
fresh_tomatoes.open_movies_page(movies)