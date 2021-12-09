from  code import *
from errors import MangaReadTypeError

class Usuario:

    '''
    Clase que representa a un usuario
    
    Attributes
    ----------
    usuario: str
        Nombre de usuario
    leidos: list[(string, float)]
        Mangas leídos por el usuario
    recomendados: list[string]
        Recomendaciones realizadas al usuario
    
    Methods
    -------
    no_leido(name)
        Función Booleana que comprueba si el manga es nuevo o no para el usuario
    add_leido(manga, nota)
        Añade un manga a la lista de mangas leídos por el usuario, lleva consigo una nota
    add_recomendado(manga)
        Añade un manga nuevo a la lista personal de recomendaciones
    '''

    def __init__(self, usuario, vistos = [], recomendaciones = []):

        '''
        Constructor de la clase Usuario

        Parameters
        ----------
        usuario: str
            Nombre de usuario
        leidos: list[(string, float)]
            Mangas leídos por el usuario
        recomendados: list[string]
            Recomendaciones realizadas al usuario
        '''

        self.usuario = usuario
        self.leidos = vistos
        self.recomendados = recomendaciones
    
    '''
    Función Booleana para determinar si un manga es nuevo para el usuario o, 
    por el contrario, es conocido

    Parameters
    ----------
    name : string
        Nombre del manga
    
    Returns
    -------
    is_new: boolean
        True: si no leyó ese manga
        False: si lo leyó
    '''

    def es_nuevo(self, name):
        is_new = True
        for manga in self.leidos:
            if manga[0] == name:
                is_new = False
                break
        
        return is_new

    '''
    Añade un manga a la lista de leídos junto con su nota
    
    Parameters
    ----------
    manga : Manga
        Manga leído a introducir en la lista
    nota : float
        Nota dada tras leer el manga
    
    Raises
    ------
    MangaReadTypeError
        Si el manga ya está en la lista
    '''
    def add_leido(self, manga, nota):

        if self.es_nuevo(manga._name):
            pareja = (manga._name, nota)
            self.leidos.append(pareja)
            manga.recalcula_media(nota)
        else:
            raise MangaReadTypeError()
            
    '''
    Añade un manga a la lista de manga recomendados al usuario
    Parameters
    ----------
    manga : Manga
        Mnaga a introducir en la lista de recomendaciones 
        
    Raises
    ------
    MangaReadTypeError
        Si el manga ya está en la lista
        '''
    def add_recomendado(self, manga):

        if self.es_nuevo(manga._name):
            if self.recomendados.count(manga._name) == 0:
                self.recomendados.append(manga._name)
        else:
            raise MangaReadTypeError()