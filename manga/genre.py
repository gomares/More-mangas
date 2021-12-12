

class Genre:
	"""

    Entidad que representa géneros de un manga.

    Attributes
    ----------
    name : str
        Nombre del manga.
    generos : list of String
        Lista de géneros que puede tener el manga.



	"""

	def __init__(self) -> None:
		"""
        	Constructor de la entidad
		"""
	
		self.generos=["SHONEN","SEINEN","SHOJO","JOSEI","KODOMO","ISEKAI","CYBERPUNK","YAOI","YURI","ECCHI","HENTAI","SPOKON","MAGICAL_GIRLS","MECHAS"]



# Ponderación de los géneros
ponderacion = {"SHONEN": 7, "SEINEN": 5, "SHOJO": 7, "JOSEI": 10, "KODOMO": 4, "ISEKAI": 7,
               "CYBERPUNK": 8, "YAOI": 9, "YURI": 9, "ECCHI": 9, "HENTAI": 10, "SPOKON": 3,
               "MAGICAL_GIRLS": 6, "MECHAS": 6}
