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
        print(f"Contacto {nombre} {telefono} {email} agregado correctamente.")

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

    #buescar por lista
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