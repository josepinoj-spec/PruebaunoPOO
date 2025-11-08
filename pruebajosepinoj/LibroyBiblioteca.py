
class Libro:
    
    def __init__(self, titulo, autor, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles

    #Disminuye una copia si hay disponibles.
    def prestar(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            return True
        else:
            return False
        
              
    #Aumenta en 1 la cantidad de copias disponibles
    def devolver(self):
        self.copias_disponibles += 1
        
    #Muestra datos del libro.
    def mostrar_informacion(self):
        
        print(f"Titulo: {self.titulo} | Autor: {self.autor} | "
              f"Copias disponibles: {self.copias_disponibles}")



class Biblioteca:
    def __init__(self, catalago):
        self.catalogo=catalago [ ]
        
    # Agrega un libro nuevo al catalogo
    def registrar_libro(self, titulo, autor, copias):
        nuevo = Libro(titulo, autor, copias)
        self.catalogo.append(nuevo)
        print(f"Libro '{titulo}' registrado correctamente.")
        
    #Muestra todos los libros registrados con sus copias
    def mostrar_catalogo(self):
        if not self.catalogo:
            print("No hay libros registrados")
            return
        
        print("\ Catalogo Completo:")
        for libro in self.catalogo:
            libro.mostrar_informacion()
        print()
            
    #  Busca un libro por titulo y lo devuelve si existe 
    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    # Intenta prestar un libro disminuyendo sus copias
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)

        if libro is None:
            print("El libro no existe en la biblioteca")
        else:
            if libro.prestar():
                print(f"Se ha prestado '{titulo}'")
            else:
                print(f"No quedan copias de '{titulo}' para prestar.")   
    
    # Registra la devolucion de un libro al catalogo
        if libro is None:
            print("Este libro no pertenece a la biblioteca.")
        else:
            libro.devolver()
            print(f"Se ha registrado la devolucion de '{titulo}'.")

    # Muestra la informacion actualizada de un libro especifico
    def estado_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        
        if libro is None:
            print("El libro no se encuentra en la biblioteca.")
        else:
            print("Estado actual del libro:")
            libro.mostrar_informacion() 
            
    def menu():
    buscar_libro = Biblioteca()

    