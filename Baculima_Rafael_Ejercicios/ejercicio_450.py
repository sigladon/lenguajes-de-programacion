socios = {}

def menu():
    print("1) Registrar socio")
    print("2) Eliminar socio")
    print("2) Añadir libro")
    print("3) Registrar préstamo")
    print("4) Registrar devolución")
    print("5) Revisar estado socio")
    print("6) Mostrar los estudiantes con calificación superior a la media")
    print("7) Pasar día")
    print("8) Salir")

def solicitar_entero(mensaje):
    return int(input(mensaje))

def agregar_socio(dni, nombre, telefono):
    socios[dni] = (nombre,telefono)

opcion_usuario = 0
dias_transcurridos_biblioteca = 0

while opcion_usuario != 8:
    menu()
    opcion_usuario = solicitar_entero(opcion_usuario)

    match opcion_usuario:
        case 1:
            dni_nuevo_socio = input("Ingrese el DNI del nuevo socio:\n")
            if socios.get(dni_nuevo_socio, "No existe") == "No existe":
                nombre_nuevo_socio = input("Ingrese el nombre del nuevo socio:\n")
                telefono_nuevo_socio = input("Ingrese el telefono del nuevo socio:\n")
                agregar_socio(dni_nuevo_socio, nombre_nuevo_socio, telefono_nuevo_socio)
                print("Se ha registrado exitosamente el nuevo socio")
            else:
                print("Ya existe un socio registrado con ese DNI")
        case 2:
            dni_socio_eliminar = input("Ingrese el DNI del nuevo socio:\n")
            if socios.get(dni_socio_eliminar, "No existe") != "No existe":
                del socios[dni_socio_eliminar]
                print("Se ha eliminado del sistema los datos de ese socio")
            else:
                print("No se encontró un socio asociado a ese DNI")



