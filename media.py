
# Import required modules
import webbrowser

# My Movie Class
class Movie():
	''' This is the Movie class that requires 3 inputs - 
	Movie Title, Movie Poster Image, Youtube trailer link '''
	# Defining the constructor
	def __init__(self, movie_title, poster_image, trailer_youtube):
			# Movie Title
			self.title = movie_title
			# Movie Poster
			self.poster_image_url = poster_image
			# Youtube trailer link
			self.trailer_youtube_url = trailer_youtube

	# Method to show the trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)