class Menu:
    def __init__(self):
        pass

    @staticmethod
    def menu():
        print("""
1) Registrar socio
2) Eliminar socio
3) Añadir libro
4) Registrar préstamo
5) Registrar devolución
6) Revisar estado socio
7) Pasar día
8) Salir
        """)

    def solicitar_entero(mensaje):
        return int(input(mensaje))
