from errors import GenreNotFoundError, MangakaTypeError
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
    puntuacion_media : float
        Puntuación media que los usuarios dieron al manga.
    lecturas : int
        Veces que fue leído el manga.

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
    get_puntuacion_media()
            Devuleve un flotante con la puntuación media del manga en cuestión.
    get_lecturas()
            Devuleve un flotante con las lecturas que tiene el manga.
   calcular_media()
            Calcula la nota media del manga.
   aniade_lectura()
            Añade una lectura al manga.

    """

    def __init__(self, name: str, genres: list, mangakas: list, num_vols: int, puntuacion_media: float, lecturas : int):
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
        puntuacion_media : float
                Puntuación media que los usuarios dieron al manga.
        lecturas : int
                Veces que fue leído el manga.
        """

        # Comprobación de errores

        # Validación géneros
        l = []
        for genre in Genre:
            l.append(genre)

        es_correcto = False
        if set(genres) <= set(l):
            es_correcto = True

        if es_correcto == False:
            #raise GenreNotFoundError()
            pass

        # Validación autores
        for mangaka in mangakas:
            if type(mangaka) != str:
                raise MangakaTypeError()

        # Una vez que los valores son correctos se establecen en la clase.
        self._name = name
        self._genres = genres
        self._mangakas = mangakas
        self._num_vols = num_vols
        self._puntuacion_media = puntuacion_media
        self._lecturas = lecturas

    def get_name(self):
        return self._name

    def get_genres(self):
        return self._genres

    def get_mangakas(self):
        return self._mangakas

    def get_num_vols(self):
        return self._num_vols

    def get_puntuacion_media(self):
        return self._puntuacion_media

    def get_lecturas(self):
        return self._lecturas

    def calcular_media(self, puntuacion_dada):
        '''
        Calcula la nota media en función de todas la cantidad de usuarios que valoraron el manga

        Parameters
        ----------
        nota: float
            Nota del manga
        '''
        self.puntuacion_media = ((self.puntuacion_media*self._lecturas+puntuacion_dada)/(self._lecturas+1))


       
    def nueva_lectura(self):
        '''
        Añade una lectura al manga
        '''
        self._lecturas += 1

