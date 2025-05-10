from src.modelo.Tienda import Tienda
from src.modelo.Compra import Compra
from src.modelo.Articulo import Articulo

from src.vista.Vista import Vista

class ControladorTienda:

    def __init__(self):
        self.vista = Vista()
        self.tienda = Tienda()
        self.compra = Compra()

    def verificar_entero(self, cadena1, cadena2):
        try:
            return int(input(cadena1))
        except:
            print(cadena2)
            self.verificar_entero(cadena1, cadena2)

    def verificar_flotante(self, cadena1, cadena2):
        try:
            return float(input(cadena1))
        except:
            print(cadena2)
            self.verificar_flotante(cadena1, cadena2)


    def main(self):
        opcion = 0

        while opcion != 6:
            self.vista.menu_inicial()
            opcion = self.verificar_entero('Ingrese opcion:', 'Opcion no valida')

            match opcion:
                case 1:
                    self.tienda.agregar_articulo(Articulo(input('Ingrese codigo:'), self.verificar_flotante('Ingrese precio:', 'Precio no valido'), self.verificar_flotante('Ingrese descuento:', 'Descuento no valido'), input('Ingrese seccion:')))

                case 2:
                    self.tienda.listar_codigos()
                    codigo = self.verificar_entero('Ingrese numero de codigo:', 'Codigo no valido')
                    self.compra.compra.append(self.tienda.obtener_codigos()[codigo - 1])

                case 3:
                    print('El total de la compra es:$', self.tienda.calcular_total(self.compra.compra))

                case 4:
                    print('Secciones que debe visitar\n', self.tienda.hallar_secciones(self.compra.compra))

                case 5:
                    if self.tienda.descuentos_por_seccion() is not None: print('Las secciones con mas de 50%\n', self.tienda.descuentos_por_seccion())

        self.tienda.guardar_articulos()


