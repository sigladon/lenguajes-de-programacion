class Perro:
    tipo = 'canino'

    def __init__(self, nombre):
        self.nombre = nombre

d = Perro('Davis')
e = Perro('Fresa')

print(d.tipo)
print(e.tipo)
print(d.nombre)
print(e.nombre)
