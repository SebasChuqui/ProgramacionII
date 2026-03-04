import math

class Estadistica:

    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom)**2 for x in self.__datos)
        return math.sqrt(suma / (len(self.__datos) - 1))


numeros = list(map(float, input("Ingrese 10 números: ").split()))

estad = Estadistica(numeros)

print(f"El promedio es {estad.promedio():.3f}")
print(f"La desviación estándar es {estad.desviacion():.3f}")