#creacion de la clase

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
