import uuid
from abc import ABC, abstractmethod

class ICarrera(ABC):
    @abstractmethod
    def get_datos(self):
        pass

    @abstractmethod
    def set_datos(self, data: object):
        pass


class Carrera(ICarrera):

    def __init__(self, nombre, categoria):
        self._id = uuid.uuid4()
        self._nombre = nombre
        self._categoria = categoria

    def get_datos(self):
        data = {self._nombre, self._categoria}
        return data

    def set_datos(self, data: object):
        self._nombre = data.nombre
        self._categoria = data.categoria
