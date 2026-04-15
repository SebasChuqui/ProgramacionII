import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas= vidas
        self.vidasIniciales= vidas
        self.record= 0
        
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
            
    def actualizarRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print("Nuevo record: ", self.record)
            
    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan: ", self.numeroDeVidas, "vidas")
            
        if self.numeroDeVidas <= 0:
            print("Perdiste")
            return False
        else:
            
            return True


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
        
    def ValidaNumero(self, num):
        return 0 <= num <= 10
    
    def generarNumero(self):
        return random.randint(0, 10)

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = self.generarNumero()
        
        print("\nAdivina el número entre 0 y 10")
        
        while self.numeroDeVidas > 0:
            num = int(input("Ingresa tu número: "))
            
            if not self.ValidaNumero(num):
                print("Número invalido")
                continue
            
            if num == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else:
                quedanVidas = self.quitaVida()
                
                if quedanVidas:
                    if num < self.numeroAAdivinar:
                        print("El número es Mayor")
                    else:
                        print("El número es Menor")
                else:
                    break
                
class JuegoAdivinarPar(JuegoAdivinaNumero):
    def ValidaNumero(self, num):
        if num % 2 != 0:
            print("Error, el número debe ser PAR")
            return False
        return 0 <= num <= 10
    
    def generarNumero(self):
        return random.choice([0,2,4,6,8,10])
    
class JuegoAdivinarImpar(JuegoAdivinaNumero):
    def ValidaNumero(self, num):
        if num % 2 == 0:
            print("Error, el número debe ser IMPAR")
            return False
        return 0 <= num <= 10
    
    def generarNumero(self):
        return random.choice([1,3,5,7,9])
    
    
class Aplicacion:
    def main(self):
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinarPar(3)
        juego3 = JuegoAdivinarImpar(3)
        
        print("\n--Juego Normal--")
        juego1.juega()  
        print("\n--Juego Pares--") 
        juego2.juega()
        print("\n--Juego Impares--")
        juego3.juega()
        
app = Aplicacion()
app.main()