participantes = [
    'Tadej Pogacar', 'Remco Evenepoel', 'Richard Carapaz', 'Jonas Vingegaard',
    'Primož Roglič', 'Jai Hindley', 'Carlos Rodríguez', 'Simon Yates',
    'Enric Mas', 'João Almeida', 'Sepp Kuss', 'Mikel Landa',
    'Julian Alaphilippe', 'Wout van Aert', 'Mathieu van der Poel', 'Mark Cavendish',
    'Egan Bernal', 'Geraint Thomas', 'Aleksandr Vlasov', 'Adam Yates'
]
tiempo = [
    [10234.5, 12678.9, 13901.3, 10456.2, 10567.8, 9987.6, 11000.1, 12111.2, 10345.7],
    [11987.0, 11345.6, 12498.7, 11420.3, 12765.4, 11123.8, 12234.5, 10567.9, 11890.2],
    [10345.8, 10456.3, 11935.0, 10358.1, 11867.3, 10145.9, 11256.0, 9876.5, 10901.4],
    [10098.3, 12012.6, 13134.9, 9987.4, 10112.5, 9654.3, 10765.4, 11876.5, 10012.9],
    [11654.9, 11124.7, 12257.0, 11278.3, 12520.6, 10991.7, 12102.8, 10456.1, 11789.5],
    [10456.7, 10567.2, 12046.1, 10470.8, 11978.5, 10257.3, 11368.4, 9987.0, 11012.6],
    [10679.2, 12902.7, 14024.5, 10590.3, 10701.4, 10011.9, 11123.0, 12234.1, 10457.8],
    [12124.9, 11458.3, 12624.8, 11546.2, 12913.7, 11247.0, 12358.1, 10691.5, 12023.9],
    [10568.3, 10679.8, 12157.6, 10581.9, 12089.2, 10369.7, 11480.8, 10102.3, 11134.7],
    [10211.6, 12157.0, 11291.3, 10121.5, 10246.7, 9776.4, 10887.5, 11998.6, 10235.1],
    [11766.2, 11235.9, 12368.4, 11390.1, 12625.3, 11103.2, 12214.3, 10567.8, 11890.6],
    [10468.4, 10579.9, 12169.1, 10492.8, 12090.7, 10381.5, 11492.6, 10114.1, 11146.9],
    [10690.8, 12914.1, 14137.3, 10704.2, 10815.1, 10132.7, 11243.8, 12354.9, 10580.2],
    [12236.5, 11570.3, 12737.1, 11657.6, 13025.4, 11359.3, 12470.4, 10803.8, 12136.2],
    [10579.6, 10691.1, 12280.0, 10604.9, 12201.5, 10479.8, 11590.9, 10212.4, 11248.3],
    [10322.7, 12258.1, 13392.7, 10233.2, 10358.3, 9887.9, 10999.0, 12110.1, 10346.5],
    [11877.3, 11346.7, 12470.5, 11419.2, 12754.7, 11112.9, 12224.0, 10579.6, 11902.3],
    [10433.2, 10544.7, 11913.5, 10422.6, 11813.3, 10121.0, 11232.1, 9854.7, 10980.1],
    [10801.4, 13125.0, 14348.3, 10815.7, 10926.6, 10243.9, 11355.0, 12466.1, 10691.5],
    [12347.9, 11680.6, 12836.7, 11768.1, 13137.6, 11471.0, 12582.1, 10914.9, 12248.7]
]

def ganador_vuelta(ciclistas, tiempos):
    tiempos_totales = [sum(tiempos[i]) for i in range(len(tiempos))]
    print(tiempos_totales)
    print(ciclistas[tiempos_totales.index(min(tiempos_totales))])

def ganador_etapa(ciclistas,tiempos,etapa):
    tiempos_etapa = [tiempos[i][etapa-1] for i in range(len(ciclistas))]
    return ciclistas[tiempos_etapa.index(min(tiempos_etapa))]

def ganadores_etapa(ciclistas,tiempos):
    for i in range(1,len(tiempos[0])+1):
        print("Etapa " + str(i) + ": " + ganador_etapa(ciclistas,tiempos,i))


opcion_usuario = 0

def calcular_numero_etapas(tiempos):
    return len(tiempos[0])

def menu():
    print("1) Obtener el ganador de la vuelta")
    print("2) Obtener el ganador de una etapa")
    print("3) Obtener el ganador por etapa")
    print("4) Salir")

def solicitar_entero(indicacion):
    return int(input(indicacion))

while opcion_usuario != 4:
    menu()
    try:
        opcion_usuario = solicitar_entero("Ingrese una opción: \n")

        match opcion_usuario:
            case 1:
                ganador_vuelta(participantes, tiempo)
            case 2:
                etapa_usuario = solicitar_entero("Ingrese el número de la etapa (1-" + str(calcular_numero_etapas(tiempo)) + ")\n")
                try:
                    if etapa_usuario > 0:
                        print(ganador_etapa(participantes, tiempo, etapa_usuario))
                    else:
                        print("Debe ingresar un número de etapa válido")
                except IndexError:
                    print("Debe ingresar un número de etapa válido")
            case 3:
                ganadores_etapa(participantes, tiempo)
            case 4:
                print("Saliendo del programa")

    except ValueError:
        print("Opción inválida")
        opcion_usuario = 0