import random
class Matriz(object):
    def __init__(self, numero_filas, numero_columnas):
        self.numero_filas = numero_filas
        self.numero_columnas = numero_columnas
        self.arreglo = [[0] * numero_columnas for i in range(numero_filas)]
        for i in range(self.numero_filas):
            for j in range(self.numero_columnas):
                self.arreglo[i][j] = random.randint(1,10)

    def __add__(self, matriz):
            resultado = Matriz(self.numero_filas, self.numero_columnas)
            for i in range(self.numero_filas):
                for j in range(self.numero_columnas):
                    resultado.arreglo[i][j] = self.arreglo[i][j] + matriz.arreglo[i][j]
            return resultado

    def __sub__(self, matriz):
        resultado = Matriz(self.numero_filas, self.numero_columnas)
        for i in range(self.numero_filas):
            for j in range(self.numero_columnas):
                resultado.arreglo[i][j] = self.arreglo[i][j] - matriz.arreglo[i][j]
        return resultado

    def imprimir_matriz(self):
        for i in range(self.numero_filas):
            fila = ""
            for j in range(self.numero_columnas):
                fila += str(self.arreglo[i][j]) + " "
            print(fila)
        print()

# Multiplicac

a = Matriz(5, 5)
a.imprimir_matriz()
b = Matriz(5, 5)
b.imprimir_matriz()

c = a+b
c.imprimir_matriz()

d = a-b
d.imprimir_matriz()