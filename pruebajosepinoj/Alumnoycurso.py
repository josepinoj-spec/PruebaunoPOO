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