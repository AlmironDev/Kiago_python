from Models.Usuario import Usuario


class UsuarioController:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, nombre, rol, phone, categoria):
        usuario = Usuario(nombre, rol, phone, categoria)
        self.usuarios.append(usuario)
        return usuario

    def get_usuarios(self):
        return self.usuarios

    def get_usuario(self, id):
        for usuario in self.usuarios:
            if usuario._id == id:
                return usuario
        return None

    def update_usuario(self, data: object):
        usuario = self.get_usuario(data["_id"])
        if usuario is not None:
            usuario._nombre = data["nombre"]
            usuario._rol = data["rol"]
            usuario._phone = data["phone"]
            usuario._categoria = data["categoria"]
            return usuario
        return None

    def delete_usuario(self, id):
        usuario = self.get_usuario(id)
        if usuario is not None:
            self.usuarios.remove(usuario)
            return usuario
        return None
