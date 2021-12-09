from manga import *
from manga import genre
from manga.manga import Manga
from user import *
from errors import *


def recomendar(usuario, mangas, generos, num_volumenes=None):
    '''
    Recomienda un manga en función a los géneros introducidos y el número de volúmenes del manga

    Parameters
    ----------
    usuario : Usuario
        Usuario que necesita recomendación
    mangas : list[Manga]
        Mangas posibles para una recomendación
    generos : list[Genre]
        Géneros elegidos por el usuario para obtener la recomendación
    num_volumenes : float, optional
        Límite de volúmenes que quieres para la recomendación

    Returns
    -------
    recomendaciones : list[Manga]
        Mangas seleccionados como recomendaciones
    '''
    a_ordenar = []
    recom_finales = []

    if len(usuario.leidos) == 0:

        for manga in mangas:
            puntuacion = 0
            
            puntuacion = sum(map((lambda x : genre.ponderacion[x] if generos.count(x) > 0 else 0), manga._genres))

            if puntuacion > 0 and (num_volumenes == None or manga._num_vols <= num_volumenes):
                puntuacion *= manga._puntuacion_media
                a_ordenar.append((manga, puntuacion))
        
        a_ordenar.sort(key= lambda x : x[1])
        for r in a_ordenar:
            recom_finales.append(r[0])
        
        recom_finales.reverse()
        recom_finales = recom_finales[0:3] #Sacamos nuestro top 3
    else: #Más adelante se implementará
        pass

    for reco in recom_finales:
        usuario.add_recomendado(reco)

    return recom_finales
