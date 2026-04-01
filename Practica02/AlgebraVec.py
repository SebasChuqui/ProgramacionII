import math

class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def producto_punto(self):
        return sum(self.a[i] * self.b[i] for i in range(len(self.a)))

    def magnitud(self, v):
        return math.sqrt(sum(x**2 for x in v))

    # ortogonales
    def perpendicular(self):
        return self.producto_punto() == 0

    # ||
    def paralelo(self):
        razones = []
        for i in range(len(self.a)):
            if self.b[i] != 0:
                razones.append(self.a[i] / self.b[i])
        return all(r == razones[0] for r in razones)

    # Proy a en b
    def proyeccion(self):
        escalar = self.producto_punto() / (self.magnitud(self.b)**2)
        return [escalar * x for x in self.b]

    def componente(self):
        return self.producto_punto() / self.magnitud(self.b)


a = [1, 2, 3]
b = [2, 4, 6]

av = AlgebraVectorial(a, b)

print("Perpendicular:", av.perpendicular())
print("Paralelo:", av.paralelo())
print("Proyección:", av.proyeccion())
print("Componente:", av.componente())