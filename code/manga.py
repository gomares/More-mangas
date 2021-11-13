# This class will be the most basic representation of the information
# managed by the application.
class Manga:

	# Builder of the class. It will create an object with the followings
	# attributes:
	# 	- Name of the manga : string
	# 	- Genres of the manga : List of strings
	# 	- Mangakas : List of strings
	# These attributes should be the main variables of the entity because
	# they uniquely represent a manga. Also, they should be privated.
	def __init__(self,name,genres,mangakas):
		self._name = name
		self._genres = genres
		self._mangakas = mangakas

	def get_name(self):
		return self._name

	def get_genre(self):
		return self._genre

	def get_mangaka(self):
		return self._mangaka