class Laberinto:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def es_valido(self, x, y):
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.matriz[x][y] == 0

def busqueda_profundidad_iterativa(laberinto, inicio, destino, max_profundidad):
    # Iterar inclusive hasta max_profundidad
    for limite in range(max_profundidad + 1):
        visitados = set()
        camino = buscar_camino(laberinto, inicio, destino, limite, visitados)
        if camino:
            return camino
    return None

def buscar_camino(laberinto, actual, destino, limite, visitados):
    x, y = actual
    
    # Caso base: llegamos al límite de profundidad
    if limite < 0:
        return None
        
    # Caso base: llegamos al destino
    if actual == destino:
        return [actual]
        
    # Si la posición no es válida o ya fue visitada
    if not laberinto.es_valido(x, y) or actual in visitados:
        return None
        
    visitados.add(actual)
    
    # Movimientos posibles: arriba, derecha, abajo, izquierda
    movimientos = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    
    for siguiente in movimientos:
        camino = buscar_camino(laberinto, siguiente, destino, limite-1, visitados)
        if camino:
            return [actual] + camino
            
    visitados.remove(actual)
    return None
