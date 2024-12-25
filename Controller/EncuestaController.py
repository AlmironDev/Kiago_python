from Models.Encuestas import Encuesta


class CarreraController:
    def __init__(self):
        self.encuestas = []

    def create_carrera(self, nombre, carrera, estudiante):
        encuesta = Encuesta(nombre, carrera, estudiante)
        self.encuestas.append(encuesta)
        return encuesta

    def get_carreras(self):
        return self.encuestas

    def get_encuesta(self, id):
        for encuesta in self.encuestas:
            if encuesta._id == id:
                return encuesta
        return None

    def update_encuesta(self, id, criterios):
        encuesta = self.get_encuesta(id)
        if encuesta is not None:
            encuesta._criterios = criterios
            return encuesta
        return None

    def delete_encuesta(self, id):
        encuesta = self.get_encuesta(id)
        if encuesta is not None:
            self.encuestas.remove(encuesta)
            return encuesta
        return None
