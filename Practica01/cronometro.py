import time
import random

class Cronometro:
    
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = 0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def iniciar(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
 
numeros = [random.randint(1, 100000) for _ in range(100000)]
cron = Cronometro()
cron.iniciar()
print("ordenando...")
seleccion(numeros)

cron.detener()

print("Tiempo en milisegundos:", cron.lapsoDeTiempo())