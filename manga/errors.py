

class GenreNotFoundError(Exception):
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

class MangaReadTypeError(Exception):
	"""
	Excepción lanzada para errores si el manga fue leído y está en la lista del user.

	Attributes
	----------
	message: str
		Texto explicativo del error.
	"""
	def __init__(self, message="El manga ya está incluido"):
		self.message = message