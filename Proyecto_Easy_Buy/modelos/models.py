
class User:
    def __init__(self, id, dni, codigo, nombre, apellido_paterno,
                 apellido_materno, correo, contrasena, estado, id_rol):
        self.nombre = id
        self.dni = dni
        self.codigo = codigo
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.contrasena = contrasena
        self.estado = estado
        self.id_rol = id_rol
