###### Ejercicio  Agenda de contacto #######

from AgendaContacto import Agenda

def mostrar_menu():
    print("\n--- MENÚ DE AGENDA ---")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Buscar por coincidencia")
    print("5. Eliminar contacto")
    print("6. Salir")

def main():
    contacto = AgendaContacto()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)

        elif opcion == "2":
            agenda.mostrar_contacto()

        elif opcion == "3":
            dato = input("Ingresa nombre o email a buscar: ")
            agenda.buscar_contacto(dato)

        elif opcion == "4":
            texto = input("Texto para búsqueda parcial: ")
            agenda.buscar_por_lista(texto)

        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


##### Aqui termina el ejercio  #######


#### Ejercio alumno y contacto  #######

from curso import Curso

def mostrar_menu():
    print("\n--- MENÚ DEL CURSO ---")
    print("1. Inscribir alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

def main():
    curso = Curso(" Estadisticas ")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del alumno: ")
            apellidos = input("Apellidos del alumno: ")
            curso.inscribir_alumno(nombre, apellidos)

        elif opcion == "2":
            curso.listar_alumnos()

        elif opcion == "3":
            nombre = input("Nombre del alumno a buscar: ")
            apellidos = input("Apellidos del alumno a buscar: ")
            alumno = curso.buscar_alumno(nombre, apellidos)
            if alumno:
                print(f"Alumno encontrado: {alumno.nombre} {alumno.apellidos}")
            else:
                print("Alumno no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del alumno a eliminar: ")
            apellidos = input("Apellidos del alumno a eliminar: ")
            curso.eliminar_alumno(nombre, apellidos)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


#####   Termino del ejercio ##########


###### Ejercio de Libro y biblioteca  ######

from biblioteca import Biblioteca

def mostrar_menu():
    print("\n--- MENÚ DE BIBLIOTECA ---")
    print("1. Registrar libro")
    print("2. Mostrar catálogo")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Estado de un libro")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            copias = int(input("Número de copias: "))
            biblioteca.registrar_libro(titulo, autor, copias)

        elif opcion == "2":
            biblioteca.mostrar_catalogo()

        elif opcion == "3":
            titulo = input("Título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)

        elif opcion == "4":
            titulo = input("Título del libro a devolver: ")
            biblioteca.devolver_libro(titulo)

        elif opcion == "5":
            titulo = input("Título del libro: ")
            biblioteca.estado_libro(titulo)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

#####Termino de ejercicio   ######




###### Ejercico Pedido   #######

from pedido import Pedido

def mostrar_menu():
    print("\n--- MENÚ DE PEDIDO ---")
    print("1. Agregar ítem")
    print("2. Mostrar ítems")
    print("3. Mostrar detalle del pedido")
    print("4. Salir")

def main():
    pedido = Pedido()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            pedido.agregar_item(nombre, precio, cantidad)

        elif opcion == "2":
            pedido.mostrar_items()

        elif opcion == "3":
            pedido.mostrar_detalle()

        elif opcion == "4":
            print("¡Pedido finalizado!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


###### Termino de ejercicio  ######


##### Ejercio catalogo de pelicula ######


from catalogo import CatalogoPeliculas

def mostrar_menu():
    print("\n--- MENÚ DE CATÁLOGO DE PELÍCULAS ---")
    print("1. Agregar película")
    print("2. Mostrar catálogo")
    print("3. Buscar por título")
    print("4. Filtrar por género")
    print("5. Salir")

def main():
    catalogo = CatalogoPeliculas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la película: ")
            genero = input("Género: ")
            año = input("Año de lanzamiento: ")
            catalogo.agregar_pelicula(titulo, genero, año)

        elif opcion == "2":
            catalogo.mostrar_catalogo()

        elif opcion == "3":
            titulo = input("Título a buscar: ")
            catalogo.buscar_por_titulo(titulo)

        elif opcion == "4":
            genero = input("Género a filtrar: ")
            catalogo.filtrar_por_genero(genero)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


#####  Termino ejercico pelicula #####


#### Ejercicio Sensor  #####


from sensor import Sensor

def mostrar_menu():
    print("\n--- MENÚ DE SENSOR ---")
    print("1. Agregar medición")
    print("2. Mostrar promedio")
    print("3. Mostrar máximo")
    print("4. Mostrar mínimo")
    print("5. Salir")

def main():
    nombre_sensor = input("Ingrese el nombre del sensor: ")
    sensor = Sensor(nombre_sensor)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = float(input("Ingrese el valor de la medición: "))
            sensor.agregar_medicion(valor)

        elif opcion == "2":
            promedio = sensor.obtener_promedio()
            if promedio is not None:
                print(f"Promedio de mediciones: {promedio:.2f}")

        elif opcion == "3":
            maximo = sensor.obtener_maximo()
            if maximo is not None:
                print(f"Valor máximo: {maximo}")

        elif opcion == "4":
            minimo = sensor.obtener_minimo()
            if minimo is not None:
                print(f"Valor mínimo: {minimo}")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


###### Termino ejercicio sensor #####


#### Ejercicio  Autentificacion Usuario  #####


from autenticacion import SistemaAutenticacion

def mostrar_menu():
    print("\n--- MENÚ DE AUTENTICACIÓN ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Verificar si usuario está registrado")
    print("4. Salir")

def main():
    sistema = SistemaAutenticacion()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            print(sistema.registrar_usuario(usuario, contrasena))

        elif opcion == "2":
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            print(sistema.login(usuario, contrasena))

        elif opcion == "3":
            usuario = input("Ingrese el nombre de usuario: ")
            print(sistema.usuario_registrado(usuario))

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


###### Termino ejercicio Autentificacion #####
