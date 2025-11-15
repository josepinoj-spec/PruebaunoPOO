
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
        self.catalogo= {}
        
    def _normalizar(self, texto):
        return texto.strip().lower()
        
    # Registrar libro
    def registrar_libro(self, titulo, autor, copias):
        titulo_nombre = self._normalizar(titulo)
        
        if titulo_nombre in self.catalogo:
            print("El libro ya existe, se actualizan las copias. ")
            self.catalogo[titulo_nombre][copias] += copias
        else:
            self.catalogo[titulo_nombre] = {
                "titulo:original" : titulo.strip(),
                "autor" : autor.strip(),
                "copias" : copias,
                "prestados" : 0
            }
        print("Libro registrado correctamente")
        self.catalogo.append(nuevo)
        print(f"Libro '{titulo}' registrado correctamente.")
        
    #Mostrar catálogo
    def mostrar_catalogo(self):
        if not self.catalogo:
            print("No hay libros registrados.")
            return
        
        for datos in self.catalogo.values():
            print(f"{datos['titulo_original']} - {datos['autor']} | "
                f"Disponibles: {datos['copias'] - datos['prestados']}")

# Prestar libro
    def prestar_libro(self, titulo):
        titulo_nombre = self._normalizar(titulo)

        if titulo_nombre not in self.catalogo:
            print("El libro no existe.")
            return
        
        libro = self.catalogo[titulo_nombre]
        disponibles = libro["copias"] - libro["prestados"]

        if disponibles > 0:
            libro["prestados"] += 1
            print("Libro prestado con éxito.")
        else:
            print("No hay copias disponibles.")

# Devolver libro
    def devolver_libro(self, titulo):
        titulo_nombre = self._normalizar(titulo)

        if titulo_nombre not in self.catalogo:
            print("El libro no existe.")
            return
        
        libro = self.catalogo[titulo_nombre]

        if libro["prestados"] > 0:
            libro["prestados"] -= 1
            print("Libro devuelto con éxito.")
        else:
            print("No hay préstamos registrados.")
            
# Estado de un libro
    def estado_libro(self, titulo):
        titulo_nombre = self._normalizar(titulo)

        if titulo_nombre not in self.catalogo:
            print("El libro no existe.")
            return
        
        libro = self.catalogo[titulo_norm]
        print(f"{libro['titulo_original']} - {libro['autor']} | "
            f"Copias: {libro['copias']} | Prestados: {libro['prestados']}")
