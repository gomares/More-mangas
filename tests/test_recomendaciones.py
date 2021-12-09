
import pytest
import sys
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./manga/')
from manga.genre import Genre
from manga.recomendaciones import recomendar
from manga.manga import Manga
from manga.user import Usuario

user_prueba = Usuario("gomares")


# Formato objeto Manga: name,genres,mangakas,num_vols, puntuacion_media, lecturas

mangas = [
Manga("One Piece", [Genre.ISEKAI, Genre.SHONEN, Genre.ECCHI], ["Eiichiro Oda"], 12, 8.5, 100),
Manga("Demon Slayer", [Genre.CYBERPUNK,Genre.ISEKAI, Genre.SEINEN], ["Koyoharu Gotouge"], 9, 9.0, 120),
Manga("Bleach Josei", [Genre.JOSEI, Genre.YAOI], ["Ryu Matsumoto"], 13, 7.5, 200),
Manga("Yuri no Yuro", [Genre.YURI, Genre.HENTAI], ["Kikiu Mikoto"], 21, 6.9, 123),
Manga("Glass Mask", [Genre.SPOKON, Genre.SHOJO], ["Suzue Miuchi"], 15, 7.3, 45),
Manga("Maison Ikkoku", [Genre.MECHAS, Genre.SHOJO], ["Rumiko Takahashi"], 5, 8.6, 67),
Manga("The Poe Clan", [Genre.YAOI, Genre.SHONEN], ["Mōto Hagio"], 8, 8.3, 80),
Manga("Star of the Giants", [Genre.SHONEN, Genre.ECCHI], ["Ikki Kajiwara"], 12, 8.1, 78),
Manga("Astro Boy", [Genre.CYBERPUNK,Genre.MAGICAL_GIRLS, Genre.MECHAS], ["Osamu Tezuka"], 15, 7.9, 54),
Manga("Golden Kamuy", [Genre.MECHAS, Genre.YURI], ["Noda Satoru"], 10, 8.0, 230)
]

def test_vistos_vacio():
    assert_that(user_prueba.leidos).is_empty()

def test_recomendaciones_vacio():
    assert_that(user_prueba.recomendados).is_empty()

def test_recomienda_shonen():
    recomendaciones = recomendar(user_prueba, mangas, [Genre.SHONEN])
    assert_that(recomendaciones).is_length(3)   #Top 3 mangas

def test_actualiza_recomendaciones_usuario():
    assert_that(user_prueba.recomendados).is_not_empty()


def test_nota_mayor():
    mayor = True
    
    for i in range(len(user_prueba.recomendados)-1):

        recomendado1 = user_prueba.recomendados[i]
        recomendado2 = user_prueba.recomendados[i+1]


        for x in mangas: #Encontrar por título los mangas recomendados par obtener su puntuación
            if x._name == recomendado1:
                m1 = x
            if x._name == recomendado2:
                m2 = x

        if m1._puntuacion_media < m2._puntuacion_media : #si el top1 resulta tener menos puntuacion que el top 2 entonces algo va mal
            mayor = False
            break

    assert_that(mayor).is_true()    #Si se hace una búsqueda por un solo género entonces devolvemos el de mayor nota


def test_genero_presente(): #En todas las recomendaciones por género está el género especificado

    presente = False

    for rec in user_prueba.recomendados:
        presente = False

        for manga in mangas:
            if rec == manga._name:
                m1 = manga

        for gen in m1._genres:
            if gen == Genre.SHONEN:
                presente = True
                break

        if not presente:
            break

    assert_that(presente).is_true()

def test_recomendaciones_kodomo_genre(): #No hay recomendaciones de un genero que no está presente en la colección de mangas
    recomendaciones = recomendar(user_prueba, mangas, [Genre.KODOMO])
    assert_that(recomendaciones).is_empty()   

def test_recomendaciones_spokon_genre():
    recomendaciones = recomendar(user_prueba, mangas, [Genre.SPOKON])
    assert_that(recomendaciones).is_length(1)

def test_recomendaciones_multiples_generos():
    recomendaciones = recomendar(user_prueba, mangas, [Genre.SHONEN, Genre.ECCHI])
    assert_that(recomendaciones).is_length(3)

def test_recomendaciones_cota_superior_3():#No hay mangas de tan solo 3 volúmenes
    recomendaciones = recomendar(user_prueba, mangas, [Genre.SHONEN], 3)
    assert_that(recomendaciones).is_empty() 

def test_recomendaciones_cota_superior_13(): #Probando si existen mangas del género
    recomendaciones = recomendar(user_prueba, mangas, [Genre.ISEKAI], 13)
    assert_that(recomendaciones).is_length(2)
