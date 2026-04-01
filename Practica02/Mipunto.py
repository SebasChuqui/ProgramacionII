import math

class MiPunto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def distanciaXY(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)

p1 = MiPunto() 
p2 = MiPunto(10, 30.5)

print("Distancia:", p1.distancia(p2))