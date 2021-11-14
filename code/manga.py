# This class will be the most basic representation of the information
# managed by the application.
class Manga:

	# Builder of the class. It will create an object with the followings
	# attributes:
	# 	- Name of the manga : string
	# 	- Genres of the manga : List of strings
	# 	- Mangakas : List of strings
	#	- Number of volumes : int
	# These attributes should be the main variables of the entity because
	# they uniquely represent a manga. Also, they should be privated.
	def __init__(self,name,genres,mangakas,num_vols):
		self._name = name
		self._genres = genres
		self._mangakas = mangakas
		self._num_vols = num_vols

	def get_name(self):
		return self._name

	def get_genres(self):
		return self._genres

	def get_mangakas(self):
		return self._mangakas

	def get_num_vols(self):
		return self._num_vols