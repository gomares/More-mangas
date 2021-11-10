import array

# The most basic class, both user and app will work with this object all time.
class Manga:
	# Builder
	def __init__(self, name, genre, mangaka):

		# Name of the Manga
		self._name = name

		# Genre of the Manga
		self._genre = genre

		# Author (mangaka) of the Manga
		self._mangaka = mangaka

		# Vector of reviews, it will contain values between 1 and 5
		self._reviews = []