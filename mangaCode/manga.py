import array

class Manga:
	def __init__(self, name, genre, mangaka):
		self._name = name
		self._genre = genre
		self._mangaka = mangaka
		self._reviews = []

	def get_name(self):
		return self._name

	def get_genre(self):
		return self._genre

	def get_mangaka(self):
		return self._mangaka

	def get_reviews(self):
		return self._reviews