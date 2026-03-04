import math

def promedio(lista):
    return sum(lista) / len(lista)

def desviacion(lista):
    prom = promedio(lista)
    suma = sum((x - prom)**2 for x in lista)
    return math.sqrt(suma / (len(lista) - 1))


numeros = list(map(float, input("Ingrese 10 números: ").split()))

print(f"El promedio es {promedio(numeros):.3f}")
print(f"La desviación estándar es {desviacion(numeros):.3f}")