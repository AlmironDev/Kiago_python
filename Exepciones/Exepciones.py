class UsuarioError(Exception):
    """Excepción base para errores relacionados con usuarios."""
    pass

class UsuarioNoEncontradoError(UsuarioError):
    """Excepción cuando un usuario no es encontrado."""
    def __init__(self, mensaje="Usuario no encontrado."):
        super().__init__(mensaje)

class DatosInvalidosError(UsuarioError):
    """Excepción para datos de usuario inválidos."""
    def __init__(self, mensaje="Los datos proporcionados son inválidos."):
        super().__init__(mensaje)

class ActualizacionFallidaError(UsuarioError):
    """Excepción para fallos en la actualización del usuario."""
    def __init__(self, mensaje="No se pudo actualizar el usuario."):
        super().__init__(mensaje)
