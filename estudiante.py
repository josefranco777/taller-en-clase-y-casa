class Estudiante:
    def __init__(self, nombre, apellido, cedula, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono

    def obtener_nombre(self):
        return f'Mi nombre es {self.nombre}'

    def obtener_apellido(self):
        return f'Mi apellido es {self.apellido}'

    def obtener_cedula(self):
        return f'Mi cédula es {self.cedula}'

    def obtener_correo(self):
        return f'Mi correo es {self.correo}'

    def obtener_telefono(self):
        return f'Mi teléfono es {self.telefono}'
    
