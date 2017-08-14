# Udacity FSND movie trailer project
Source code and details for a Movie Trailer website.

## Prerequisites
1. [Python](http://www.python.org) should be installed
2. Git should be installed or access to Github

## Installing the code
1. Clone the repository using
```
git clone https://github.com/datechie/movie_trailer.git
```

## Source Code Details
The repository has 3 source code files:
#### media.py
* This file contains the Media class definition
* This has 3 inputs - Movie Title, Movie Poster Image, Movie Trailer Youtub URL
* This class has one method to show the youtube trailer - show_trailer

#### fresh_tomatoes.py
* This is the Udacity provided code to create the Movies trailer webpage

#### entertainment_center.py
* This file contains the definitions of muliple movie instance details
* It also contains the definition of a movie list that is used as input to the fresh_tomatoes open_movies_page function

## How to Run
* cd movie_trailer
* ```python entertainment_center.py```

## Output

The command run above should open a new webpage titled **Fresh Tomatoes Movie Trailers** and should display the posters of the movies. Clicking each poster will open the youtube trailer for that movie.
