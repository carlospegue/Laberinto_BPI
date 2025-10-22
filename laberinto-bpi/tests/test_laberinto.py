import pytest
from src.laberinto_bpi import Laberinto, busqueda_profundidad_iterativa

def test_laberinto_simple():
    mapa = [
        [0,0],
        [0,0]
    ]
    laberinto = Laberinto(mapa)
    inicio = (0,0)
    destino = (1,1)
    
    camino = busqueda_profundidad_iterativa(laberinto, inicio, destino, 5)
    assert camino is not None
    assert len(camino) > 0
    assert camino[0] == inicio
    assert camino[-1] == destino

def test_laberinto_sin_solucion():
    mapa = [
        [0,1],
        [1,0]
    ]
    laberinto = Laberinto(mapa)
    inicio = (0,0)
    destino = (1,1)
    
    camino = busqueda_profundidad_iterativa(laberinto, inicio, destino, 5)
    assert camino is None

def test_posicion_invalida():
    mapa = [
        [0,0],
        [0,0]
    ]
    laberinto = Laberinto(mapa)
    assert not laberinto.es_valido(-1, 0)
    assert not laberinto.es_valido(0, -1)
    assert not laberinto.es_valido(2, 0)
    assert not laberinto.es_valido(0, 2)
