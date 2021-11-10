import array

class Manga:
	def __init__(self, name, genre, mangaka):
		self._name = name
		self._genre = genre
		self._mangaka = mangaka
		self._reviews = []