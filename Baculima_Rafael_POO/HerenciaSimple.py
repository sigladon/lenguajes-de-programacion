class Instrumento:
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estas tocando música")

    def romper(self):
        print("Esto lo pagas tú")
        print("El precio es $", self.precio)

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass


a = Bateria(1200)
a.romper()

class Terrestre:
    def desplazar(self):
        print("El animal anda")

class Acuatico:
    def desplazar(self):
        print("El animal nada")

class Cocodrilo(Terrestre, Acuatico):
    pass

coco = Cocodrilo()
coco.desplazar()
