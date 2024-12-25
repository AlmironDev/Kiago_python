import uuid
from abc import ABC, abstractmethod

class IEncuesta(ABC):
    @abstractmethod
    def get_datos(self):
        pass

    @abstractmethod
    def set_datos(self, data: object):
        pass


class Encuesta(IEncuesta):

    def __init__(self, nombre, carrera, estudiante):
        self._id = uuid.uuid4()
        self._nombre = nombre
        self._carrera = carrera
        self._estudiante = estudiante

    def get_datos(self):
        data = {self._id, self._nombre, self._carrera, self._criterios, self._estudiante}
        return data

    def set_datos(self,data:object):
        self._carrera = data.carrera
        self._estudiante = data.estudiante
        self._criterios = data.criterios
