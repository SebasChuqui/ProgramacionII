class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        
    def mostrarInfo(self):
        print(f"Autor: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        
class Estudiante:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre
        
    def mostrarInfo(self):
        print(f"Matricula: {self.matricula}")
        print(f"Nombre: {self.nombre}")
        
class Prestamo:
    def __init__(self, fprestamo, fdevolucion, estudiante, libro):
        self.fprestamo = fprestamo
        self.fdevolucion = fdevolucion
        self.estudiante = estudiante
        self.libro = libro
        
    def mostrarInfo(self):
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Libro: {self.libro.titulo}")
        print(f"Fecha préstamo: {self.fprestamo}")
        print(f"Fecha devolución: {self.fdevolucion}")        

class Libro:
    #composicion
    class Pagina:
        def __init__(self, nropagina, contenido):
            self.nropagina = nropagina
            self.contenido = contenido
            
        def mostrarPagina(self):
            print(f"página {self.nropagina}: {self.contenido}")
            
    def __init__(self, titulo, isbn, paginas):
        self.titulo = titulo
        self.isbn = isbn
        #composicion, las paginas no existen sin el libro
        self.paginas = []
        numero=1 
        for contenido in paginas:
            pagina = Libro.Pagina(numero, contenido)
            self.paginas.append(pagina)
            numero += 1
            
    def leer(self):
        print(f"leer libro: {self.titulo}")
        for i in self.paginas:
            i.mostrarPagina()
      
class Biblioteca:
    #composicion
    class Horario:
        def __init__(self, dapertura, hapertura, hcierre):
            self.dapertura = dapertura
            self.hapertura = hapertura
            self.hcierre = hcierre
            
        
        def mostrarHorario(self):
            print("Horario de atención")
            print(f"Días: {self.dapertura}")
            print(f"Apertura: {self.hapertura}")
            print(f"Cierre: {self.hcierre}")
    def __init__(self, nombre):
        self.nombre=nombre
        #agregacion
        self.libros= []
        self.autores= []
        #composicion
        self.horario= Biblioteca.Horario("Lunes a Viernes", "08:00", "20:00")
        self.prestamos=[]
    
    #agregacion
    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"Libro: {libro.titulo} Agregado")
    
    #agregacion
    def agregarAutor(self, autor):
        self.autores.append(autor)
        print(f"Autor: {autor.nombre} registrado")

    #asociacion
    def prestarLibro(self, estudiante, libro, fprestamo, fdevolucion):
        prestamo = Prestamo(fprestamo, fdevolucion, estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"Libro: {libro.titulo}, prestado a {estudiante.nombre}")        
        
    def mostrarEstado(self):
        print(f"ESTADO DE LA BIBLIOTECA \n Biblioteca: {self.nombre} ")
        self.horario.mostrarHorario()
        print("LIBROS: ")
        for i in self.libros:
            print(f" - {i.titulo}")
            
        print("AUTORES: ")
        for n in self.autores:
            print(f" - {n.nombre}")
            
        print("PRÉSTAMOS ACTIVOS: ")
        for j in self.prestamos:
            j.mostrarInfo()
        
    def cerrarBiblioteca(self):
        print("La biblioteca está cerrando")
        self.prestamos.clear()
        print("Todos los préstamos fueron eliminados.") 

libro1 = Libro("Python Básico", "111-AAA", ["Introducción a Python", "Variables y datos", "Funciones"])
libro2 = Libro("POO en Python", "222-BBB", [ "Clases", "Objetos", "Herencia"])
libro3 = Libro("Asociaciones en POO", "333-CCC", ["Asociacion", "Agregacion", "Composicion"])

autor1 = Autor("Juan Pérez", "Peruano")
autor2 = Autor("Ana López", "Argentina")
autor3 = Autor("Jhonny Felipez", "Boliviano")

estudiante1 = Estudiante("2025001", "Carlos Mendoza")
estudiante2 = Estudiante("1895276", "Aaron Manci")

biblioteca = Biblioteca("Biblioteca UMSA")

biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)
biblioteca.agregarLibro(libro3)


biblioteca.agregarAutor(autor1)
biblioteca.agregarAutor(autor2)
biblioteca.agregarAutor(autor3)


biblioteca.prestarLibro(estudiante1, libro1, "10/05/2026", "17/05/2026")
biblioteca.prestarLibro(estudiante2, libro3, "11/05/2026", "18/05/2026")
biblioteca.prestarLibro(estudiante1, libro2, "12/05/2026", "19/05/2026")

biblioteca.mostrarEstado()

libro1.leer()
libro2.leer()
libro3.leer()

biblioteca.cerrarBiblioteca()

biblioteca.mostrarEstado()
