import uuid
from abc import ABC, abstractmethod

class IUsuario(ABC):
    @abstractmethod
    def get_datos(self):
        pass

    @abstractmethod
    def set_datos(self, data: object):
        pass


class Usuario(IUsuario):

    def __init__(self, nombre, rol, phone, categoria):
        self._id :uuid = uuid.uuid4()
        self._nombre :str = nombre 
        self._rol: str = rol
        self._phone: int = phone
        self._categoria: str = categoria

    def get_datos(self):
        data = {
            "_id": self._id,
            "nombre": self._nombre,
            "categoria": self._categoria,
            "rol": self._rol,
            "phone": self._phone,
        }
        return data

    def set_datos(self, data: object):
        self._nombre: str = data["nombre"]
        self._categoria: str = data["categoria"]
        # self._password = data["password"]
        self._rol: str = data["rol"]
        self._phone: int = data["phone"]
        return True 
