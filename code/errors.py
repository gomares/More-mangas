class GenreNotFound(Exception):
	"""
	Excepción lanzada para errores si el género introducido no se encuentra
	en el enumerado Genre.

	Attributes
	----------
	message: str
		Texto explicativo del error.
	"""
	def __init__(self, message="El género no es correcto porque no se encuentra entre los géneros admitidos."):
		self.message = message

class MangakaTypeError(Exception):
	"""
	Excepción lanzada para errores si el mangaka introducido no es de tipo
	string.

	Attributes
	----------
	message: str
		Texto explicativo del error.
	"""
	def __init__(self, message="El mangaka no es un tipo de objeto válido (debe ser string)."):
		self.message = message