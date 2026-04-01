import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, r):
        return Vector3D(self.x * r, self.y * r, self.z * r)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        m = self.magnitud()
        return Vector3D(self.x/m, self.y/m, self.z/m)

    def producto_punto(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def producto_cruz(self, other):
        return Vector3D(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def es_perpendicular(self, other):
        return self.producto_punto(other) == 0

    def es_paralelo(self, other):
        cruz = self.producto_cruz(other)
        return cruz.x == 0 and cruz.y == 0 and cruz.z == 0

    def proyeccion(self, other):
        escalar = self.producto_punto(other) / (other.magnitud()**2)
        return other * escalar

    def componente(self, other):
        return self.producto_punto(other) / other.magnitud()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(2, 4, 6)
v3 = Vector3D(-2, 1, 0)

print("v1:", v1)
print("v2:", v2)

print("Suma:", v1 + v2)
print("Escalar:", v1 * 2)

print("Magnitud v1:", v1.magnitud())
print("Normal v1:", v1.normal())

print("Producto punto:", v1.producto_punto(v2))
print("Producto cruz:", v1.producto_cruz(v3))

print("¿Perpendicular?:", v1.es_perpendicular(v3))
print("¿Paralelo?:", v1.es_paralelo(v2))

print("Proyección de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en v2:", v1.componente(v2))