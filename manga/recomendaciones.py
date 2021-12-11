from manga import *
from manga import genre
from manga.manga import Manga
from user import *
from errors import *



def recomendar_nuevo_lector( mangas, generos, num_volumenes=None):
    '''
    Calcula recomendaciones para el caso de un usuario nuevo en la aplicación.

    Parameters
    ----------
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

    for manga in mangas:
        puntuacion = 0
        
        puntuacion = sum(map((lambda x : genre.ponderacion[x] if generos.count(x) > 0 else 0), manga._genres))

        if puntuacion > 0 and (num_volumenes == None or manga._num_vols <= num_volumenes):
            puntuacion *= manga._puntuacion_media
            a_ordenar.append((manga, puntuacion))
    
    a_ordenar.sort(key= lambda x : x[1],reverse = True)
    for r in a_ordenar:
        recom_finales.append(r[0]) #Pensando en hacerlo con objetos manga para luego no buscarlos por nombre y perder eficiencia
    

    recom_finales = recom_finales[0:3] #Sacamos nuestro top 3
    return recom_finales

def recomendar_lector_experimentado(): #Pertenece al siguiente Milestone
    pass




def recomendar( usuario, mangas, generos, num_volumenes=None):
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

    if len(usuario.leidos) == 0: #El usuario es totalmente nuevo
        recom_finales = recomendar_nuevo_lector(mangas,generos,num_volumenes)
    else: #Más adelante se implementará el caso para el lector experimentado
        recom_finales = recomendar_lector_experimentado()

    for reco in recom_finales:
        usuario.add_recomendado(reco)

    return recom_finales
