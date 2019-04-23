import argparse
import resource
from collections import deque
from estado import Estado

estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]
nodo_objetivo = Estado
estado_inicial = list()
tamanio_tablero = 0
lado_tablero = 0

profundidad_maxima_busqueda = 0
tamanio_maximo_frontera = 0

movimientos = list()
costs = set()

def bfs(estado_inicio):
    global tamanio_maximo_frontera, nodo_objetivo, profundidad_maxima_busqueda

    explorado, queue = set(), deque([Estado(estado_inicio, None, None, 0, 0, 0)])

    while queue:
        nodo = queue.popleft()
        explorado.add(nodo.map)

        if nodo.estado == estado_objetivo:
            nodo_objetivo = nodo
            return queue

        vecinos = expandir(nodo)

        for vecino in vecinos:
            if vecino.map not in explorado:
                queue.append(vecino)
                explorado.add(vecino.map)
                if vecino.profundidad > profundidad_maxima_busqueda:
                    profundidad_maxima_busqueda += 1

        if len(queue) > tamanio_maximo_frontera:
            tamanio_maximo_frontera = len(queue)

def expandir(nodo):
    vecinos = list()

    vecinos.append(Estado(movimiento(nodo.estado, 1), nodo, 1, nodo.profundidad + 1, nodo.costo + 1, 0))
    vecinos.append(Estado(movimiento(nodo.estado, 2), nodo, 2, nodo.profundidad + 1, nodo.costo + 1, 0))
    vecinos.append(Estado(movimiento(nodo.estado, 3), nodo, 3, nodo.profundidad + 1, nodo.costo + 1, 0))
    vecinos.append(Estado(movimiento(nodo.estado, 4), nodo, 4, nodo.profundidad + 1, nodo.costo + 1, 0))

    nodes = [vecino for vecino in vecinos if vecino.estado]

    return nodes

def movimiento(estado, posicion):
    nuevo_estado = estado[:]
    indice = nuevo_estado.index(0)

    if posicion == 1:  # Up
        if indice not in range(0, lado_tablero):
            temp = nuevo_estado[indice - lado_tablero]
            nuevo_estado[indice - lado_tablero] = nuevo_estado[indice]
            nuevo_estado[indice] = temp
            return nuevo_estado
        else:
            return None

    if posicion == 2:  # Down
        if indice not in range(tamanio_tablero - lado_tablero, tamanio_tablero):
            temp = nuevo_estado[indice + lado_tablero]
            nuevo_estado[indice + lado_tablero] = nuevo_estado[indice]
            nuevo_estado[indice] = temp
            return nuevo_estado
        else:
            return None

    if posicion == 3:  # Left
        if indice not in range(0, tamanio_tablero, lado_tablero):
            temp = nuevo_estado[indice - 1]
            nuevo_estado[indice - 1] = nuevo_estado[indice]
            nuevo_estado[indice] = temp
            return nuevo_estado
        else:
            return None

    if posicion == 4:  # Right
        if indice not in range(lado_tablero - 1, tamanio_tablero, lado_tablero):
            temp = nuevo_estado[indice + 1]
            nuevo_estado[indice + 1] = nuevo_estado[indice]
            nuevo_estado[indice] = temp
            return nuevo_estado
        else:
            return None

def retroceso():
    nodo_actual = nodo_objetivo

    while estado_inicial != nodo_actual.estado:
        if nodo_actual.movimiento == 1:
            movimiento = 'Up'
        elif nodo_actual.movimiento == 2:
            movimiento = 'Down'
        elif nodo_actual.movimiento == 3:
            movimiento = 'Left'
        else:
            movimiento = 'Right'

        movimientos.insert(0, movimiento)
        nodo_actual = nodo_actual.padre
    return movimientos


def exportar(frontera):
    global movimientos

    movimientos = retroceso()

    print("Camino al objetivo: " + str(movimientos))
    print("Costo del camino: " + str(len(movimientos)))

def leer(configuracion):
    global tamanio_tablero, lado_tablero

    datos = configuracion.split(",")

    for elemento in datos:
        estado_inicial.append(int(elemento))

    tamanio_tablero = len(estado_inicial)
    lado_tablero = int(tamanio_tablero ** 0.5)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tablero')
    args = parser.parse_args()
    leer(args.tablero)
    frontera = bfs(estado_inicial)
    exportar(frontera)

if __name__ == '__main__':
    main()
