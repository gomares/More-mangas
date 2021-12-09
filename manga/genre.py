from enum import Enum, auto

class Genre(Enum):
	"""

	Objeto valor que representa el género de un manga

	"""
	SHONEN = auto()
	SEINEN = auto()
	SHOJO = auto()
	JOSEI = auto()
	KODOMO = auto()
	ISEKAI = auto()
	CYBERPUNK = auto()
	YAOI = auto()
	YURI = auto()
	ECCHI = auto()
	HENTAI = auto()
	SPOKON = auto()
	MAGICAL_GIRLS = auto()
	MECHAS = auto()


# Ponderación de los géneros
ponderacion = {Genre.SHONEN: 7, Genre.SEINEN: 5, Genre.SHOJO: 7, Genre.JOSEI: 10, Genre.KODOMO: 4, Genre.ISEKAI: 7,
               Genre.CYBERPUNK: 8, Genre.YAOI: 9, Genre.YURI: 9, Genre.ECCHI: 9, Genre.HENTAI: 10, Genre.SPOKON: 3,
               Genre.MAGICAL_GIRLS: 6, Genre.MECHAS: 6}
