denominaciones = [500,200,100,50,20,10,5,2,1]

def calcular_desgloce(cantidad_ingreso):
    for denominacion in denominaciones:
        if denominacion > cantidad_ingreso:
            continue
        cantidad_denominacion_actual = cantidad_ingreso // denominacion
        tipo_denominacion = " billetes" if (denominacion > 2) else " monedas"
        print(str(cantidad_denominacion_actual) + tipo_denominacion + " de " + str(denominacion) + " euros")
        cantidad_ingreso -= cantidad_denominacion_actual * denominacion

cantidad_usuario = int(input("Ingrese la cantidad de euros a transformar (sin decimales)\n"))
calcular_desgloce(cantidad_usuario)

# Realizar los siguientes ejercicios:
# 110, 116, 270