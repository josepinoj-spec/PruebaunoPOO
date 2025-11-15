#creacion de la clase

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre.strip()
        self.mediciones = []
    
#Agregamos la medicion
    def agregar_medicion(self,valor: float):
        self.mediciones.append(float(valor))
        print(f"Medición {valor} agregada al sensor '{self.nombre}'.")
    
#Para obtener la medicion promedio   
    def obtener_promedio(self):
        if not self.mediciones:
            print("No hay mediciones registradas." )
        return None
    return sum(self.mediciones) / len(self.mediciones)

#Obtener el valor maximo de la medicion
    def obtener_maximo(self):
        if not self.mediciones:
            print("No hay mediciones registradas.")
            return None
        return max(self.mediciones)

#Obtener el valor minimo de la medicion            
    def obtener_minimo(self):
        if not self.mediciones:
            print("No hay mediciones registradas.")
            return None
        return min(self.mediciones)
        
#Mostrar el nombre de la medicion
    def mostrar_nombre(self):       
        return self.nombre
