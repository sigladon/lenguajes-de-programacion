# Cálculo del área de un triángulo
def area_triangulo(base,altura):
    return base * altura / 2

base = int(input("Ingrese la longitud en metros de la base: \n"))
altura = int(input("Ingrese la longitud en metros de la altura: \n"))
print("El área del triángulo es de " + str(area_triangulo(base,altura)) + " m^2")
