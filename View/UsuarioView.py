from Controller.UsuarioController import UsuarioController
from Exepciones.Exepciones import ActualizacionFallidaError, DatosInvalidosError, UsuarioNoEncontradoError
from Exepciones.Valid_data import validar_tipos
"""
Creacion de un nuevo usuario a la empresa Kiago
"""


class UsuarioView:
    def __init__(self):
        self.controller = UsuarioController()

    def create_user(self, nombre: str, rol: str, phone: int, categoria: str):
        try:
            validar_tipos(
                valores={"nombre": nombre, "rol": rol, "phone": phone, "categoria": categoria},
                tipos={"nombre": str, "rol": str, "phone": int, "categoria": str},
            )
            usuario = self.controller.crear_usuario(nombre, rol, phone, categoria)
            return usuario.get_datos()  # Devolver los datos del usuario
        except ValueError as e:
            raise DatosInvalidosError(f"Error al crear usuario: {e}")

    def get_users(self):
        return [usuario.get_datos() for usuario in self.controller.get_usuarios()]

    def get_user(self, id):
        try:
            if id is None:
                raise UsuarioNoEncontradoError("No se ha proporcionado una ID válida.")
            usuario = self.controller.get_usuario(id)
            if usuario is None:
                raise UsuarioNoEncontradoError("Usuario no encontrado.")
            return usuario.get_datos()
        except ValueError as e:
            raise DatosInvalidosError(f"Error al pedir usuario: {e}")

    def update_user(self, data: object):
        try:
            usuario = self.controller.update_usuario(data)
            if usuario is None:
                raise ActualizacionFallidaError("No se pudo actualizar el usuario.")
            return usuario.set_datos(data)
        except ValueError as e:
            raise DatosInvalidosError(f"Error al actualizar usuario: {e}")

    def delete_user(self, id):
        try:
            if id is None:
                raise UsuarioNoEncontradoError("No se ha proporcionado una ID válida.")
            usuario = self.controller.delete_usuario(id)
            if usuario is None:
                raise UsuarioNoEncontradoError("Usuario no encontrado.")
            return usuario
        except ValueError as e:
            raise DatosInvalidosError(f"Error al eliminar usuario: {e}")
