import math

def calcular_combinaciones(n,m):
    if n < m:
        return None
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m))

print("Cálculo de combinaciones tomando m elementos de un conjunto con n elementos")
n = int(input("Ingrese un valor para n (elementos del conjunto)\n"))
m = int(input("Ingrese un valor para m (elementos a tomar)\n"))

print("El número de combinaciones es de " + str(int(calcular_combinaciones(n,m))))
