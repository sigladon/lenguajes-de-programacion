def solicitar_entero(texto):
    return int(input(texto))

def solicitar_real(texto):
    return float(input(texto))

lista_calificaciones = {}
nota_aprobacion = 70

def agregar_estudiante_calificacion(estudiante, calificacion):
    lista_calificaciones[estudiante] = calificacion

def mostrar_lista_estudiantes_calificacion():
    print(lista_calificaciones)

def calcular_media_calificaciones():
    calificaciones = lista_calificaciones.values()
    return sum(calificaciones)/len(calificaciones)

def calcular_numero_aprobados():
    numero_aprobados = 0
    for estudiante in lista_calificaciones:
        if lista_calificaciones[estudiante] >= nota_aprobacion:
            numero_aprobados += 1
    return numero_aprobados

def mostrar_mejores_calificaciones():
    mejores_calificaciones = {}
    for estudiante in lista_calificaciones:
        if lista_calificaciones[estudiante] >= 85:
            mejores_calificaciones[estudiante] = lista_calificaciones[estudiante]
    return mejores_calificaciones

def mostrar_calificaciones_superiores_media():
    mejores_calificaciones = {}
    for estudiante in lista_calificaciones:
        if lista_calificaciones[estudiante] >= calcular_media_calificaciones():
            mejores_calificaciones[estudiante] = lista_calificaciones[estudiante]
    return mejores_calificaciones

def consultar_calificacion_estudiante(estudiante):
    print(estudiante + " " + lista_calificaciones[estudiante])

def menu():
    print("1) Añadir estudiante y calificación")
    print("2) Mostrar lista de estudiantes con sus calificaciones")
    print("3) Calcular la media de las calificaciones")
    print("4) Calcular el número de aprobados")
    print("5) Mostrar los estudiantes con mejor calificación")
    print("6) Mostrar los estudiantes con calificación superior a la media")
    print("7) Consultar la nota de un estudiante")
    print("8) Salir")

opcion_usuario = 0

while opcion_usuario != 8:
    menu()
    try:
        opcion_usuario = solicitar_entero("Ingrese una opción: \n")

        match opcion_usuario:
            case 1:
                nombre_estudiante = input("Ingrese el nombre del estudiante\n")
                calificacion_estudiante = solicitar_real("Ingrese la calificación del estudiante\n")
                if 0 <= calificacion_estudiante <= 100:
                    agregar_estudiante_calificacion(nombre_estudiante, calificacion_estudiante)
                else:
                    print("La calificación debe estar entre 0 y 100")
            case 2:
                mostrar_lista_estudiantes_calificacion()
            case 3:
                print("La media de calificaciones es de " + str(calcular_media_calificaciones()))
            case 4:
                print("El número de aprobados es de " + str(calcular_numero_aprobados()))
            case 5:
                print(mostrar_mejores_calificaciones())
            case 6:
                print(mostrar_calificaciones_superiores_media())
            case 7:
                nombre_estudiante = input("Ingrese el nombre del estudiante\n")
                try:
                    print("El estudiante " + nombre_estudiante + " obtuvo una calificación de " + str(consultar_calificacion_estudiante(nombre_estudiante)))
                except KeyError:
                    print("No se encontró el estudiante")
            case 8:
                print("Saliendo del programa")

    except ValueError:
        print("Opción inválida")
        opcion_usuario = 0
