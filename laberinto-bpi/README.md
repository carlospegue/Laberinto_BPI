# Laberinto con Búsqueda de Profundidad Iterativa

Este proyecto implementa un solucionador de laberintos usando el algoritmo de Búsqueda de Profundidad Iterativa (BPI).

## Características
- Encuentra el camino más corto en un laberinto
- Manejo de obstáculos (paredes)
- Visualización del camino encontrado

## Uso
```python
from src.laberinto_bpi import Laberinto, busqueda_profundidad_iterativa

# Crear laberinto
mapa = [
    [0,0,0,1],
    [1,1,0,1],
    [0,0,0,0],
    [1,1,1,0]
]

laberinto = Laberinto(mapa)
inicio = (0,0)
destino = (3,3)

# Encontrar camino
camino = busqueda_profundidad_iterativa(laberinto, inicio, destino, 10)
```


