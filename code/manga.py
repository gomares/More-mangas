from errors import GenreNotFound
from genre import Genre

class Manga:
	"""
	Entidad que representa un manga.

	Attributes
	----------
	name : str
		Nombre del manga.
	genres : list of Genre
		Lista de géneros a los que pertenece el manga.
	mangakas : list of string
		Lista de mangakas que han desarrollado la obra.
	num_vols : int
		Número de volúmenes en los que se compone el manga.
	
	Methods
	-------
	get_name()
		Devuelve el nombre del manga.
	get_genres()
		Devuelve una lista con objetos de tipo Genre.
	get_mangakas()
		Devuelve una lista de strings con los nombres de los autores.
	get_num_vols()
		Devuelve un entero con el número de volúmenes de la obra.

	"""

	def __init__(self,name: str,genres: list,mangakas: list,num_vols: int):
		"""
		Constructor de la entidad

		Parameters
		----------
		name : str
			Nombre del manga.
		genres : list of Genre
			Lista de géneros a los que pertenece el manga.
		mangakas : list of string
			Lista de mangakas que han desarrollado la obra.
		num_vols : int
			Número de volúmenes en los que se compone el manga.
		"""

		# Comprobación de errores
		for genre in genres:
			if genre not in Genre:
				raise GenreNotFound()

		for mangaka in mangakas:
			if type(mangaka) != str:
				raise MangakaTypeError()

		# Una vez que los valores son correctos se establecen en la clase.
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