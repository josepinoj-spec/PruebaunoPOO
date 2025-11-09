
class SistemaAutenticacion:
    def __init__(self):
        # Diccionario para almacenar usuarios: {usuario: contraseña}
        self.usuarios = {}

    def registrar_usuario(self, usuario, contrasena):
        if usuario in self.usuarios:
            return f" El usuario '{usuario}' ya existe. Registro cancelado."
        else:
            self.usuarios[usuario] = contrasena
            return f" Usuario '{usuario}' registrado exitosamente."

    def login(self, usuario, contrasena):
        if usuario not in self.usuarios:
            return f" Acceso rechazado. El usuario '{usuario}' no está registrado."

        if self.usuarios[usuario] == contrasena:
            return f" Acceso autorizado. Bienvenido '{usuario}'."
        else:
            return f" Acceso rechazado. Contraseña incorrecta."

    def usuario_registrado(self, usuario):
        if usuario in self.usuarios:
            return f" El usuario '{usuario}' está registrado."
        else:
            return f" El usuario '{usuario}' NO está registrado."
        
        