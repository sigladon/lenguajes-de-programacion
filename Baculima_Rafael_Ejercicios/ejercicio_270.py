caracteres = ["T", "R", "W","A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
def calcular_ultima_letra(dni):
    return caracteres[dni % 25]

try:
    print(calcular_ultima_letra(int(input("Ingrese un DNI: "))))
except ValueError:
    print("El DNI no es valido")