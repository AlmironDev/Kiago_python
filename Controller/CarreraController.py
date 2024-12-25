from Models.Carreras import Carrera


class CarreraController:
    def __init__(self):
        self.carreras = []
    
    def create_carrera(self, nombre, categoria):
        carrera = Carrera(nombre, categoria)
        self.carreras.append(carrera)
        return carrera
    
    def get_carreras(self):
        return self.carreras
    
    def get_carrera(self,id):
        for carrera in self.carreras:
            if carrera._id == id:
                return carrera
        return None
    
    def update_carrera(self,id,categoria):
        carrera = self.get_carrera(id)
        if carrera is not None:
            carrera._categoria = categoria
            return carrera
        return None
    
    def delete_carrera(self,id):
        carrera = self.get_carrera(id)
        if carrera is not None:
            self.carreras.remove(carrera)
            return carrera
        return None
