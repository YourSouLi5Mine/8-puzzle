
class Estado:

    def __init__(self, estado, padre, movimiento, profundidad, costo, llave):
        self.estado = estado
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad
        self.costo = costo
        self.llave = llave

        if self.estado:
            self.map = ''.join(str(e) for e in self.estado)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map
