from laberinto_bpi import Laberinto, busqueda_profundidad_iterativa

def main():
    # Crear un laberinto (0 = camino libre, 1 = pared)
    mapa = [
        [0,0,0,1,0,0,1,0],
        [1,1,0,1,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [1,1,1,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]
    ]

    laberinto = Laberinto(mapa)
    inicio = (0,0)    # Punto inicial
    destino = (7,7)   # Punto final

    # Validar inicio/destino
    if not laberinto.es_valido(*inicio):
        print("Inicio inválido (pared o fuera de rango).")
        return
    if not laberinto.es_valido(*destino):
        print("Destino inválido (pared o fuera de rango).")
        return

    # Buscar camino: aumentar profundidad máxima si es necesario
    camino = busqueda_profundidad_iterativa(laberinto, inicio, destino, 50)

    if camino:
        print("¡Camino encontrado! Longitud:", len(camino)-1, "movimientos")
        visualizar_laberinto(mapa, camino)
    else:
        print("No se encontró camino. Prueba aumentando el límite de profundidad.")

def visualizar_laberinto(mapa, camino):
    # Crear una copia del mapa para no modificar el original
    visual = [fila[:] for fila in mapa]
    
    # Marcar el camino con asteriscos
    for x, y in camino:
        visual[x][y] = '*'
    
    # Imprimir el laberinto
    print("\nLaberinto resuelto:")
    for fila in visual:
        print(" ".join(['*' if c == '*' else '█' if c == 1 else '·' for c in fila]))

if __name__ == "__main__":
    main()
