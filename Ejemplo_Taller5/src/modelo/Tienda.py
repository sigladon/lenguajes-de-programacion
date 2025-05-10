import pickle
from functools import reduce

class Tienda:
    def __init__(self):
        self.articulos = {}
        self.cargar_articulos()

    def listar_codigos(self):
        return [print(f'{numero}. {codigo}') for numero, codigo in enumerate(self.articulos, start= 1)]

    def obtener_codigos(self):
        return [codigo for codigo in self.articulos]

    def agregar_articulo(self, articulo):
        if articulo.codigo not in self.articulos: self.articulos[articulo.codigo] = articulo

    def calcular_precio_articulo(self, codigo):
        return self.articulos[codigo].precio - self.articulos[codigo].precio * self.articulos[codigo].descuento/100

    def calcular_total(self, codigos):
        return sum(list(map(lambda articulo: self.calcular_precio_articulo(articulo), codigos)))

    def hallar_secciones(self, codigos):
        return '\n'.join(reduce(lambda lista_visita, articulo: lista_visita + [self.articulos[articulo].seccion] if self.articulos[articulo].seccion not in lista_visita else None, codigos,[]))

    def descuentos_por_seccion(self):
        return reduce(lambda dicc, articulo: dicc.update({self.articulos[articulo].seccion: dicc.get(self.articulos[articulo].seccion, 0) + 1}), list(filter(lambda articulo: self.articulos[articulo].descuento > 50, list(self.articulos.keys()))), {})


    def guardar_articulos(self):
        try:
            with open('./data/articulos.dat', 'wb') as file:
                pickle.dump(self.articulos,file)
        except:
            print('Error con el archivo')

    def cargar_articulos(self):
        try:
            with open('./data/articulos.dat', 'rb') as file:
                self.articulos = pickle.load(file)
        except:
            print('Error con el archivo')

