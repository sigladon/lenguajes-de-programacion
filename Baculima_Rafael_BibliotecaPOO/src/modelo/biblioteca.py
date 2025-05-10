class Biblioteca:
    def __init__(self):
        self.coleccion_libros = {}
        self.socios = {}

    def agregar_libro(self, libro):
        self.coleccion_libros[libro.nombre] = libro

    def registrar_socio(self, socio):
        self.socios[socio.nombre] = socio

    def eliminar_socio(self, dni_socio_a_eliminar):
        try:
            del self.socios[dni_socio_a_eliminar]
            return True
        except NameError:
            return False
