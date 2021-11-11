# This class represents the user who will use the app
class User:

	# Builder
	def __init__(self, nickname, name, surnames, email, passwd):

		# Unique Nickname
		self._nickname = nickname

		# Name of the user
		self._name = name

		# Surnames of the user
		self._surnames = surnames

		# Unique email of the user
		self._email = email
		
		# Vector of pairs review:Manga, it will be useful to make
		# recommendations after.
		self.reviews = [] 