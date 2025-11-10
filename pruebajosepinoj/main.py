# Agenda de contactos
class Contacto:
    def __init__(self, nombre,telefono,email):
        
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

            
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

    
class Agenda:
    def __init__(self):
        self.contactos = []

#agregar contactos
    def agregar_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre}{telefono}{email} agregado correctamente.")

#Mostrar contactos 
    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("\n Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

#Buscar contactos y si no se encuntrab indicarlo
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == dato.lower() or contacto.email.lower() == dato.lower():
                    print(f" Contacto encontrado:\n{contacto}")
            return
            
        print(f"No se encontró ningún contacto con el nombre '{nombre} {telefono} {email}'.")


#Eliminar contacto
    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto '{nombre}' eliminado correctamente.")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

    #buscar por lista
    def buscar_por_lista(self, texto):
        encontrados = []
        texto = texto.lower()

        for contacto in self.contactos:
            if (texto in contacto.nombre.lower()
                or texto in contacto.email.lower()):
                encontrados.append(contacto)

        if not encontrados:
            print(f"No se encontraron contactos que coincidan con '{texto}'.")
        else:
            print(f"\n Se encontraron {len(encontrados)} contacto(s):")
            for c in encontrados:
                print(c)

        #  mostrar estado actualizad
        self.mostrar_contactos()
        
        
#Alumno y Curso
class Alumno:
    def __init__(self, nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        
class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []  #lista de alumnos

    #inscribir un alumno
    def inscribir_alumno(self, nombre_alumno, apellidos_alumno):
        if self.buscar_alumno(nombre_alumno) is not None:
            print(f"El alumno {"nombre_alumno"} ya está inscrito.")
            return
        
        nuevo_alumno = Alumno(nombre_alumno, apellidos_alumno)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno {"nombre_alumno"} inscrito en el curso.")
        
        # Buscar un alumno por nombre y apellido
    def buscar_alumno(self, nombre_alumno, apellidos_alumno):
            for alumno in self.alumnos:
                if alumno.nombre == nombre_alumno and alumno.apellidos == apellidos_alumno:
                    return alumno
                return None
                
        #eliminar alumno
    def eliminar_alumno(self, nombre_alumno, apellidos_alumno):
            alumno =self.buscar_alumno(nombre_alumno, apellidos_alumno)
            if alumno is None:
                print(f"El alunmo '{nombre_alumno} {apellidos_alumno}' No esta inscrito en a curso")
            else:
                self.alumnos.remove(alumno)    
            print(f"Alumno '{nombre_alumno} {apellidos_alumno}' ha sido eliminado del curso.")
                
    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos inscritos en el curso.")
        return

    print("\nLista de alumnos inscritos:")
    for alumno in self.alumnos:
        print(f"- {alumno.nombre} {alumno.apellidos}")
    print()
    

#Libro y Biblioteca
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
        self.catalogo=catalago 
        
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

# Pedido e item
class Item:
    def __init__ (self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
                
    def calcular_subtotal(self):
        return f"self.precio * self.cantidad"

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Subtotal: ${self.calcular_subtotal():.2f}"


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - $ {self.precio}"

class Pedido:
    def __init__(self):
        self.items = []

#Agregar un nuevo item
    def agregar_item(self, nombre, precio, cantidad):
        nuevo_item = Item(nombre, precio, cantidad)
        self.items.append(nuevo_item)
        print(f"Ítem '{nombre_producto} x {precio} x {cantidad}' agregado al pedido.")

#Mostrar listado producto
    def mostrar_items(self):
        if not self.items:
            print(" El pedido está vacío.")
        else:
            print("\n Lista de ítems en el pedido:")
            for item in self.items:
                print(item)
                
# calcular sub total   
    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

#Mostrar detalle
    def mostrar_detalle(self):
        print("\n DETALLE DEL PEDIDO")
        if not self.items:
            print("El pedido está vacío.")
            return

        for item in self.items:
            print(item)

        print(f"\nTOTAL A PAGAR: $ {self.calcular_total()}")
        
# Pelicula y catalogo
class Pelicula:
    def __init__(self, titulo, genero, año_lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self.año_lanzamiento = año_lanzamiento

    def __str__(self):
        return f"{self.titulo} ({self.año_lanzamiento}) - Género: {self.genero}"


class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = []

#Agregar pelicula
    def agregar_pelicula(self, titulo, genero, año_lanzamiento):
        nueva = Pelicula(titulo, genero, año_lanzamiento)
        self.peliculas.append(nueva)
        print(f"Película '{titulo} {genero} {año_lanzamiento}' agregada correctamente.")

#Mostar catalogo
    def mostrar_catalogo(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            print("\n Catálogo de Películas:")
            for p in self.peliculas:
                print(f"- {p}")

#filtro por titulo
    def buscar_por_titulo(self, titulo):
        resultados = [p for p in self.peliculas if p.titulo.lower() == titulo.lower()]
        if resultados:
            print("\n Película encontrada:")
            for p in resultados:
                print(f"- {p}")
        else:
            print(f" No se encontró ninguna película con el título '{titulo}'.")

#filtro por genero
    def filtrar_por_genero(self, genero):
        resultados = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if resultados:
            print(f"\n Películas del género '{genero}':")
            for p in resultados:
                print(f"- {p}")
        else:
            print(f"No hay películas del género '{genero}'.")


# Sensor y mediciones
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        elf.mediciones = []
    
#Agregamos la medicion
    def agregar_medicion(self,valor):
        self.mediciones.append(valor)
        print(f"Medición {valor} agregada al sensor '{self.nombre}'.")
    
#Para obtener la medicion promedio   
    def obtener_promedio(self):
        if not self.mediciones:
            return "No hay mediciones registradas."
        return sum(self.mediciones) / len(self.mediciones)

#Obtener el valor maximo de la medicion
    def obtener_maximo(self):
        if not self.mediciones:
            return "No hay mediciones registradas."
        return max(self.mediciones)

#Obtener el valor minimo de la medicion            
    def obterner_minimo(self):
        if not self.mediciones:
            return "No hay mediciones registradas."
        return min(self.mediciones)
        
#Mostrar el nombre de la medicion
    def mostrar_nombre(self):       
        return self.nombre

# Usuario y autentificacion
class SistemaAutenticacion:
    def __init__(self):
        # Diccionario para almacenar usuarios: {usuario: contraseña}
        self.usuarios = {}

#Regitar usuario
    def registrar_usuario(self, usuario, contrasena):
        if usuario in self.usuarios:
            return f" El usuario '{usuario}' ya existe. Registro cancelado."
        else:
            self.usuarios[usuario] = contrasena
            return f" Usuario '{usuario}' registrado exitosamente."

#Login Usuario
    def login(self, usuario, contrasena):
        if usuario not in self.usuarios:
            return f" Acceso rechazado. El usuario '{usuario}' no está registrado."

        if self.usuarios[usuario] == contrasena:
            return f" Acceso autorizado. Bienvenido '{usuario}'."
        else:
            return f" Acceso rechazado. Contraseña incorrecta."

#Usuario registrado
    def usuario_registrado(self, usuario):
        if usuario in self.usuarios:
            return f" El usuario '{usuario}' está registrado."
        else:
            return f" El usuario '{usuario}' NO está registrado."
        
        