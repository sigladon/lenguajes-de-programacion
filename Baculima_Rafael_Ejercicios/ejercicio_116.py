import math

opcion_usuario = 0
vectorA = [0.0, 0.0, 0.0]
vectorB = [0.0, 0.0, 0.0]

def verificar_vectores():
    return longitud_vector(vectorA) != 0 and longitud_vector(vectorB) != 0

def menu():
    print("1) Introducir el primer vector: " + str(vectorA))
    print("2) Introducir el segundo vector: " + str(vectorB))

    if verificar_vectores():
        print("3) Calcular la suma")
        print("4) Calcular la diferencia")
        print("5) Calcular el producto escalar")
        print("6) Calcular el producto vectorial")
        print("7) Calcular el ángulo (en grados) entre ellos")
        print("8) Calcular la longitud")

    print("9) Finalizar")

def submenu4():
    print("1) Primer vector - Segundo vector")
    print("2) Segundo vector - Primer vector")

def submenu6():
    print("1) Primer vector X Segundo vector")
    print("2) Segundo vector X Primer vector")

def submenu8():
    print("1) Primer vector")
    print("2) Segundo vector")

def solicitar_entero(indicacion):
    return int(input(indicacion))

def solicitar_real(indicacion):
    return float(input(indicacion))

def sumar_vectores(vector1, vector2):
    return [vector1[i]+vector2[i] for i in range(0,3)]

def restar_vectores(vector1, vector2):
    return [vector1[i]-vector2[i] for i in range(0,3)]

def producto_escalar(vector1, vector2):
    total = 0
    for i in range(0,3):
        total += vector1[i]*vector2[i]
    return total

def producto_vectorial(vector1, vector2):
    return [
        vector1[1]*vector2[2]-vector1[2]*vector2[1],
        vector1[2]*vector2[0]-vector1[0]*vector2[2],
        vector1[0]*vector2[1]-vector1[1]*vector2[0]
    ]

def longitud_vector(vector):
    return math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])

def angulo_entre_vectores(vector1, vector2):
    return 180/math.pi * (producto_escalar(vector1, vector2)/(longitud_vector(vector1)*longitud_vector(vector2)))


while opcion_usuario != 9:
    menu()
    try:
        opcion_usuario = solicitar_entero("Ingrese la opción deseada\n")

        match opcion_usuario:
            case 1:
                vectorA[0] = solicitar_real("Ingrese el componente x\n")
                vectorA[1] = solicitar_real("Ingrese el componente y\n")
                vectorA[2] = solicitar_real("Ingrese el componente z\n")
            case 2:
                vectorB[0] = solicitar_real("Ingrese el componente x\n")
                vectorB[1] = solicitar_real("Ingrese el componente y\n")
                vectorB[2] = solicitar_real("Ingrese el componente z\n")
            case 3:
                if verificar_vectores():
                    resultado = sumar_vectores(vectorA, vectorB)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 4:
                if verificar_vectores():
                    submenu4()
                    subopcion4 = solicitar_entero("Ingrese la opción: (por defecto 1)\n")
                    resultado = restar_vectores(vectorB, vectorA) if subopcion4 == 2 else producto_vectorial(vectorA, vectorB)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 5:
                if verificar_vectores():
                    resultado = producto_escalar(vectorA, vectorB)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 6:
                if verificar_vectores():
                    submenu6()
                    subopcion6 = solicitar_entero("Ingrese la opción: (por defecto 1)\n")
                    resultado = producto_vectorial(vectorB, vectorA) if subopcion6 == 2 else producto_vectorial(vectorA, vectorB)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 7:
                if verificar_vectores():
                    resultado = angulo_entre_vectores(vectorA, vectorB)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 8:
                if verificar_vectores():
                    submenu8()
                    subopcion8 = solicitar_entero("Ingrese la opción: (por defecto 1)\n")
                    resultado = longitud_vector(vectorB) if subopcion8 == 2 else longitud_vector(vectorA)
                    print(str(resultado))
                else:
                    print("Opción inválida")
            case 9:
                print("Saliendo del programa")
    except ValueError:
        print("Opción inválida, intente de nuevo")
        opcion_usuario = 0